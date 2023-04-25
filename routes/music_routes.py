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

@music_route.get("/lib/{id}", response_model=Library)
async def get_lib_by_id(id: str):
    lib = db.librarys.find_one({'tempId': id})
    if not lib: 
        raise HTTPException('Playlist non trouver', status_code=404)
    return lib


@music_route.put("/music/insert/{id}")
async def insert_lib(id: str, music: Music):
    db.musics.insert_one(dict(music))
    m = db.musics.find_one({"tempId": music.tempId})
    if not m:
        raise HTTPException('Playlist non trouver', status_code=404)
    db.librarys.update_one({"tempId": id}, {'$push': {'musics': m}})
    return {"Insertion réussi"}

@music_route.put("/lib/insert")
async def insert_lib(lib: Library):
    db.librarys.insert_one(dict(lib))
    library = db.librarys.find_one({"tempId": lib.tempId})
    if not library: 
        raise HTTPException('Playlist non trouver', status_code=404)
    db.users.update_one({"mail": lib.mail}, {'$push': {'librarys': library}})
    return {"Insertion réussi"}
