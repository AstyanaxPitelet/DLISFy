from pydantic import BaseModel

class AuthUser(BaseModel):
    mail: str 
    password: str 