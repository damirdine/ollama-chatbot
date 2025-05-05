import os
import uvicorn

from dotenv import load_dotenv
load_dotenv()

PORT = int(os.getenv("PORT", 8000))

def main():
    uvicorn.run("app.main:app", port=PORT)