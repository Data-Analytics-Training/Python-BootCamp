import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    texts = [
        {
            "title": "What is Flask",
            "content": "Flask is a lightweight Python Web framework",
        },
        {"title": "Learning Jinja2 ", "content": "The templates engine is very useful"},
        {"title": "Virtual Environment", "content": "Isolating dependencies is great"},
    ]
    return templates.TemplateResponse(request, "index.html", {"texts": texts})


@app.get("/users")
async def users(request: Request):
    list_users = [
        {"name": "Jack", "active": True},
        {"name": "Jill", "active": False},
        {"name": "Jim", "active": True},
    ]
    return templates.TemplateResponse(request, "users.html", {"users": list_users})


@app.get("/products")
async def products(request: Request):
    categories = [
        {"name": "Electronic", "products": ["Laptop", "Phone", "Tablet"]},
        {"name": "Book", "products": ["Novel", "Poetry", "History"]},
    ]

    return templates.TemplateResponse(
        request, "products.html", {"categories": categories}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
