from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.chat import router as chat_router

app = FastAPI(
    title="Ollama Chatbot API",
    description="Chatbot local basé sur Ollama + FastAPI avec streaming SSE",
    version="0.1.0"
)
templates = Jinja2Templates(directory="app/templates")

@app.get(
    "/",
    response_class=HTMLResponse
)
async def index(request : Request):
    return templates.TemplateResponse("index.html", {"request":request})


app.include_router(router=chat_router, prefix="/api")