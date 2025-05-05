# scripts/start.py
import os
import uvicorn

# PORT = 8000

def main():
    uvicorn.run("app.main:app")
