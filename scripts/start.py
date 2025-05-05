import os
import uvicorn

from dotenv import load_dotenv
load_dotenv()

PORT = int(os.getenv("PORT", 8000))
HOST = (os.getenv("HOST", "127.0.0.1"))

def main():
    uvicorn.run("app.main:app",host=HOST, port=PORT)