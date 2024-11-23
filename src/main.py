from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="src/templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.jinja", {"request": request})


@app.get("/favicon.ico")
async def favicon():
    return RedirectResponse("/static/favicon.ico")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
