
from bson import ObjectId
from pydantic import BaseModel
from models.music_model import Music

class Library(BaseModel):
    tempId: str
    title: str 
    img: str
    mail: str
    musics: list[Music] = []