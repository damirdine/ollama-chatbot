from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.chat import chat_endpoint

app = FastAPI(title="hello", default_response_class=JSONResponse)


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


app.include_router(chat_endpoint)