from fastapi import FastAPI

app = FastAPI(
    title="hello",
)

@app.get(
    "/",
)
def index():
    return {
        "msg": "<h1>Bienvenue sur l'application de chat avec Ollama/Deepseek !</h1>"
    }
