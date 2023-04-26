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

@music_route.get("/lib/{id}", response_model=Library, status_code=200)
async def get_lib_by_id(id: str):
    lib = db.librarys.find_one({'tempId': id})
    if not lib: 
        raise HTTPException(status_code=404, detail='Playlist non trouver')
    return lib


@music_route.put("/music/insert/{id}", status_code=201)
async def insert_music(id: str, music: Music):
    result = db.musics.insert_one(dict(music))
    if not result.acknowledged:
        raise HTTPException(status_code=500, detail='Une erreur est survenue')

    m = db.musics.find_one({"tempId": music.tempId})
    if not m:
        raise HTTPException(status_code=500, detail='Une erreur est survenue')
    
    if m['music'] == music.music:
        db.musics.delete_one({"tempId": music.tempId})
        raise HTTPException(status_code=500, detail='Titre déjà existant')
    
    db.librarys.update_one({"tempId": id}, {'$push': {'musics': m}})
    return {"Insertion réussi"}

@music_route.put("/lib/insert", status_code=201)
async def insert_lib(lib: Library):
    result = db.librarys.insert_one(dict(lib))

    if not result.acknowledged:
        raise HTTPException(status_code=500, detail='Une erreur est survenue')

    library = db.librarys.find_one({"tempId": lib.tempId})
    if not library: 
        raise HTTPException(status_code=500, detail='Une erreur est survenue')
    
    db.users.update_one({"mail": lib.mail}, {'$push': {'librarys': library}})
    return {"Insertion réussi"}
