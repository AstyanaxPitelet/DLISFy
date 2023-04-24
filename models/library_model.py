
from bson import ObjectId
from pydantic import BaseModel

class Library(BaseModel):
    tempId: str
    title: str 
    img: str
    mail: str
    musics: list | None = []