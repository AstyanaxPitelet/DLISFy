from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from routes.user_routes import user_route
from routes.music_routes import music_route
from internal.admin_routes import admin_route

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

# Tableau des origins possible
origins = [
    "http://localhost",
    "http://localhost:8080",
    
]

app = FastAPI()
app.include_router(user_route)
app.include_router(music_route)
app.include_router(admin_route)

# Configuration du middlware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('home.html', {
        "request": request,
        "hello": "Bonjour et Bienvenue sur l'API de DLISFy"
    })




