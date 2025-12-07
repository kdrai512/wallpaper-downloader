from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 1. Serve the main page
count = 0
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,"count":count})

# 2. Serve JUST the update (the fragment)
@app.post("/clicked", response_class=HTMLResponse)
async def clicked_button():
    # We simulate some logic here
    global count
    count=count+1

    return f"{count}"
