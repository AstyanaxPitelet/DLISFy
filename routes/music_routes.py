from fastapi import APIRouter, Form, UploadFile, File, HTTPException
from pymongo import MongoClient
import uuid

from models.user_model import User
from models.library_model import Library
from models.music_model import Music 

IMAGEDIR = "uploads/img-lib/"

music_route = APIRouter()

client = MongoClient(host="localhost", port=27017)
db = client.likemusic

@music_route.put("/lib/insert")
async def insert_lib(lib: Library):
    db.librarys.insert_one(dict(lib))
    library = db.librarys.find_one({"tempId": lib.tempId})
    db.users.update_one({"mail": lib.mail}, {'$push': {'librarys': library}})
    return {"Insertion réussi"}
