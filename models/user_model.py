from pydantic import BaseModel
from models.library_model import Library

class User(BaseModel):
    mail: str 
    name: str 
    firstname: str 
    password: str 
    sexe: str 
    dateNaiss: str
    pays: str
    librarys: list[Library] = []