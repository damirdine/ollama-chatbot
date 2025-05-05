# scripts/start.py
import os
import uvicorn

from dotenv import DotEnv
dotenv = DotEnv()

if os.path.exists(".env"):
    dotenv = DotEnv(".env")
    PORT = dotenv.get("PORT")
else:
    PORT = os.getenv("PORT", 8000)

def main():
    uvicorn.run("app.main:app", port=PORT)
