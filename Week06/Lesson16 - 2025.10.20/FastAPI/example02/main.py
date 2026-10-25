from datetime import datetime

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/user/{username}")
async def user(request: Request, username: str):
    today = datetime.now().strftime("%Y-%m-%d")
    return templates.TemplateResponse(
        request, "user.html", {"username": username.capitalize(), "today": today}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
