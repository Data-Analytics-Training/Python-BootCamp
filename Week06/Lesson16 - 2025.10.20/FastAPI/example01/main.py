import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# A FastAPI application object has been created.
app = FastAPI()


# FastAPI supports asynchronous programming, which allows for better performance and scalability. The async keyword is used to define asynchronous functions, which can be awaited using the await keyword. This allows for non-blocking I/O operations, such as database queries or API calls, to be performed without blocking the main thread of execution.
# Main page url
@app.get("/", response_class=HTMLResponse)
@app.get("/index", response_class=HTMLResponse)
async def index():
    return "Welcome to Python Bootcamp Course"


# about page
@app.get("/about", response_class=HTMLResponse)
async def about():
    return "This is a simple FastAPI application (with async support). #About page"


# user contact page
@app.get("/contact/{name}", response_class=HTMLResponse)
async def contact(name: str):
    return f"{name}'s contact details here."


@app.get("/year/{year_}", response_class=HTMLResponse)
async def year(year_: int):
    return f"Year {year_} is a leap year."


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
