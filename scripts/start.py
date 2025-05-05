# scripts/start.py
import os
import uvicorn

PORT = os.getenv("PORT", 8000)

def main():
    uvicorn.run("app.main:app", port=PORT)
