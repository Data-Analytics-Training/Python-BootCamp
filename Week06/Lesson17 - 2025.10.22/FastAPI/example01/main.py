import uvicorn
from fastapi import FastAPI, Form, Request
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


# * Long version of the contact route, which is commented out below. It is replaced by a single route that handles both GET and POST requests.
# @app.get("/contact")
# async def contact(request: Request):
#     return templates.TemplateResponse(request, "contact.html")
#
#
# @app.post("/contact")
# async def contact(request: Request, name: str = Form(...)):
#     message = f"Thank you, {name}"
#     return templates.TemplateResponse(request, "contact.html", {message: message})


# * Short version to combine the two contact routes into one route that handles both
# GET and POST
@app.api_route("/contact", methods=["POST", "GET"])
async def contact(request: Request):
    if request.method == "POST":
        form = await request.form()
        message = f"Thank you, {form['name']}"
        return templates.TemplateResponse(request, "contact.html", {"message": message})
    return templates.TemplateResponse(request, "contact.html")


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse(request, "404.html", status_code=404)

    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
