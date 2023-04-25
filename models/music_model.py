
from pydantic import BaseModel

class Music(BaseModel):
    tempId: str 
    title: str 
    artiste: str
    duree: float 
    music: str 
    