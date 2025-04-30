from fastapi import FastAPI

app = FastAPI(
    title="hello",
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
