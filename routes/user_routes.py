from datetime import datetime, timedelta
from typing import Union, Annotated
from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pymongo import MongoClient

from jose import JWTError, jwt
import bcrypt

from models.user_model import User
from models.auth_user_model import AuthUser
from models.token_data_model import TokenData
from models.token_model import Token

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")



from lib.message import Message
msg = Message()

user_route = APIRouter()

client = MongoClient(host="localhost", port=27017)
db = client.likemusic


def hash_password(password): 
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(passwordSasie, passwordDb):
    return bcrypt.checkpw(passwordSasie, passwordDb)

def get_user(mail):
    return db.users.find_one({"mail": f"{mail}"})

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        print("username :  " + username)
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

@user_route.get("/user/current", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

@user_route.post("/user/login", response_model=Token)
def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    print(form_data.username)
    user = authenticate_user(form_data.username, form_data.password.encode('utf-8'))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['mail']}, expires_delta=access_token_expires
    )
    return { "access_token": access_token, "token_type": "bearer" }
   

#Route de connexion utlisateur
@user_route.post("/user/insert")
async def insert_user(user: User):
    message = {}
    try:
        userDb = db.users.find_one({"mail": f"{user.mail}"})
        if userDb != None: 
            if userDb['mail'] == user.mail:
                message = {
                    "message": msg.get_register()['error']['1'],
                    "success": False
                }
            else: 
                user.password = hash_password(user.password)
                result = db.users.insert_one(dict(user))
                message = {
                    "message": msg.get_register()['message'],
                    "success": True
                }
        else: 
            user.password = hash_password(user.password)
            result = db.users.insert_one(dict(user))
            message = {
                "message": msg.get_register()['message'],
                "success": True
            }
    except HTTPException: 
        message = {
            "message": msg.get_register()['error']['0'],
            "success": False
        }
    return message