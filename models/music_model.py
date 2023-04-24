
from pydantic import BaseModel

class Music(BaseModel):
    title: str 
    duree: float 
    mp: str 
    