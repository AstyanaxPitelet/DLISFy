from datetime import datetime, timedelta
from typing import Union, Annotated
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, Request, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from pymongo import MongoClient

from jose import JWTError, jwt
import bcrypt

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from models.user_model import User
from models.auth_user_model import AuthUser
from models.token_data_model import TokenData
from models.token_model import Token

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

from lib.message import Message
msg = Message()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/admin/login")

from models.admin_model import Admin

admin_route = APIRouter(
    prefix="/admin"
)

client = MongoClient(host="localhost", port=27017)
db = client.likemusic

templates = Jinja2Templates(directory="templates")


def hash_password(password): 
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(passwordSasie, passwordDb):
    return bcrypt.checkpw(passwordSasie, passwordDb)

def get_user(username):
    user = db.admin.find_one({"username": username})
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=msg.get_default(),
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None): 
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user['password']):
        return False
    return user

# Permet la récupération de l'utlisateur connecter
@admin_route.get("/current", response_model=Admin)
async def read_users_me(current_user: Annotated[Admin, Depends(get_current_active_user)]):
    return current_user

@admin_route.get('/login', response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse('login.html', {
        "request": request,
    })  

@admin_route.post('/log', response_class=HTMLResponse)
async def login_page(request: Request, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password.encode('utf-8'))

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=msg.get_login()['error'],
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['username']}, expires_delta=access_token_expires
    )

    users = db.users.find()

    if not users:
        raise HTTPException(
            status_code=404, 
            detail="Aucun utlisateur trouver"
        )

    return templates.TemplateResponse('admin.html', { 
        "request": request,
        "users": users,
        "access_token": access_token, "token_type": "bearer"
    })

class UserId(BaseModel):
    id: str

@admin_route.delete('/user/delete', status_code=204)
async def delete_user(userId: UserId):
    print(userId.id)
    result = db.users.delete_one({"_id": ObjectId(userId.id)})
    if not result.acknowledged:
        raise HTTPException(status_code=500, detail="Un probléme est survenue")
    return {"infos": "L'utlisateur a étais supprimer avec succès"} 