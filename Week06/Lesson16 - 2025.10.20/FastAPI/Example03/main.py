import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse(request, "about.html")


@app.get("/user/{username}")
async def user(request: Request, username: str):
    return templates.TemplateResponse(
        request, "user.html", {"username": username.capitalize()}
    )


@app.get("/main")
async def main(request: Request):
    return RedirectResponse(url=request.url_for("index"), status_code=307)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse(request, "404.html", status_code=404)

    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
