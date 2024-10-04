import asyncio
from typing import Annotated
from fastapi import FastAPI, Request, Form, UploadFile, BackgroundTasks
from fastapi.templating import Jinja2Templates
import pandas as pd
import time

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get("/items/{id}")
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(request=request, name="home.html", context={"id": id})
                         
@app.get("/item/getdata")
async def read_items(request: Request):
    return templates.TemplateResponse(request=request, name="get.html")

@app.post('/item/create')
async def get_items(request: Request,name: Annotated[str, Form()]):
    print(name)
    return templates.TemplateResponse(request=request, name="get.html")

def dum():
    print("Printed")

async def write_file(path:str, content):
    try:
        # await asyncio.sleep(5)
        loop = asyncio.get_event_loop()
        loop.call_later(3,dum)
        # loop.run_forever()
        data_file = open(path, 'wb')
        # content = file.file.read()
        data_file.write(content)
    except Exception as e:
        print(f'Error: {e}')

@app.post('/upload')
async def upload_file(request: Request,background_tasks: BackgroundTasks ,file: UploadFile):
    path = f"/home/sarthakkalyani/Documents/{file.filename}"
    content = file.file.read()
    # await asyncio.sleep(2)
    background_tasks.add_task(write_file,path,content)
    # await asyncio.sleep(2)
    return {'message':f'File uploaded'}

def write_notification(email: str, message=""):
    time.sleep(3)
    print(f"emel:{email}")
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}

