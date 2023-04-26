from bson import ObjectId
from fastapi import APIRouter, HTTPException, Request, Form
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from models.admin_model import Admin

admin_route = APIRouter(
    prefix="/admin"
)

client = MongoClient(host="localhost", port=27017)
db = client.likemusic

templates = Jinja2Templates(directory="templates")

@admin_route.post('/login', response_class=HTMLResponse)
async def dashboard(request: Request):
    pass 

@admin_route.get('/dashboard', response_class=HTMLResponse)
async def dashboard(request: Request):
    users = db.users.find()

    if not users:
        raise HTTPException(
            status_code=404, 
            detail="Aucun utlisateur trouver"
        )

    return templates.TemplateResponse('admin.html', {
        "request": request,
        "users": users
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