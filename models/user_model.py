
from pydantic import BaseModel

class User(BaseModel):
    mail: str 
    name: str 
    firstname: str 
    password: str 
    sexe: str 
    dateNaiss: str
    pays: str 