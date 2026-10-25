import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

todos = [
    {"id": 1, "mission": "Learn FastAPI", "completed": True},
    {"id": 2, "mission": "Study Jinja2", "completed": False},
    {"id": 3, "mission": "Build virtual environment", "completed": False},
    {"id": 4, "mission": "Make a ToDo list", "completed": True},
]


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {"todos": todos})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
