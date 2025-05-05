# scripts/start.py
import uvicorn

from dotenv import DotEnv
dotenv = DotEnv()

PORT = dotenv.get("PORT") or 8000

def main():
    uvicorn.run("app.main:app", port=PORT)
