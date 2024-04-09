# python3 -m venv .
# source ./bin/activate
# pip3 install fastapi uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount('/files', StaticFiles(directory="uploads"), name="static")
app.mount('/web', StaticFiles(directory="html"), name="webfiles")

@app.get('/')
async def root():
    return {"message": "Welcome to ReDI School DCP Course"}
