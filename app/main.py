from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.chat import router as chat_router

app = FastAPI(
    title="Ollama Chatbot API",
    description="Chatbot local basé sur Ollama + FastAPI avec streaming SSE",
    version="0.1.0"
)

@app.get(
    "/",
)
def index():
    return {
        "message": "Bienvenue sur l'application de chat avec Ollama / Deepseek !",
        "endpoints": {
            "api": "/api",
            "docs": "/docs",
            "chat_html": "/ (via HTML si activé)",
        },
    }


app.include_router(router=chat_router, prefix="/api")