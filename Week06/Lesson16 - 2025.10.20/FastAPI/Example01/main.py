from importlib import reload

import uvicorn
from fastapi import FastAPI

# A FastAPI application object has been created.
app = FastAPI()


@app.get("/")
async def home():
    return "Welcome to Python Bootcamp Course"


@app.get("/home")
async def home_alt():
    return await home()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
