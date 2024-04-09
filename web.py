from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Example dictionary for accessing details of an endpoint
# like a blogpost url showing the specific blog post details
clothes = {
    "gucci": {
        "name": "Gucci",
        "color": "Blue"
    },
    "dolce": {
        "name": "Dolce & Gabbana",
        "color": "Red"
    }
}

# This defines the directory where the template html files will be saved
templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get('/clothes', response_class=HTMLResponse)
async def cloth_list(request: Request):
    # Adding a bit of error handling for when the id does not exist in our store
    # Also, the second parameter of templates.TemplateResponse is the context and
    # it MUST always contain the request key, otherwise the app will crash
    return templates.TemplateResponse(
        "index.html", {"request": request, "data": clothes}
    )

@app.get('/clothes/{id}', response_class=HTMLResponse)
async def cloth(request: Request, id: str):
    # Adding a bit of error handling for when the id does not exist in our store
    # Also, the second parameter of templates.TemplateResponse is the context and
    # it MUST always contain the request key, otherwise the app will crash
    if not id in clothes:
        return templates.TemplateResponse("error.html", {"request": request})
    return templates.TemplateResponse(
        "details.html", {"request": request, "data": clothes[id]}
    )
