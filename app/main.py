from fastapi import FastAPI
from fastapi.responses import JSONResponse

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
