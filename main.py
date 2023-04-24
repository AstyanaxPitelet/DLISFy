from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.user_routes import user_route
from routes.music_routes import music_route


# Tableau des origins possible
origins = [
    "http://localhost",
    "http://localhost:8080",
    
]

app = FastAPI()
app.include_router(user_route)
app.include_router(music_route)

# Configuration du middlware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "test"}




