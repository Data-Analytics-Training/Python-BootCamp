import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

contacts = [
    {"name": "Jack", "surname": "Dow"},
    {"name": "Jim", "surname": "Down"},
]


@app.api_route("/", methods=["GET", "POST"])
async def index(request: Request):
    if request.method == "POST":
        form_data = await request.form()
        name = form_data.get("name", "").strip()
        surname = form_data.get("surname", "").strip()
        if name and surname:
            contacts.append({"name": name, "surname": surname})
        return templates.TemplateResponse(request, "index.html", {"contacts": contacts})

    return templates.TemplateResponse(request, "index.html", {"contacts": contacts})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
