from typing import Annotated
from fastapi import FastAPI, Request, Form, UploadFile, BackgroundTasks
from fastapi.templating import Jinja2Templates
import pandas as pd
import uvicorn

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

@app.post('/upload')
async def upload_file(request: Request, file: UploadFile):
    try:
        path = f"/home/sarthakkalyani/Documents/{file.filename}"

        # with open(path,'wb') as f:
        #     f.write(file.file.read())
        data_file = open(path,'wb')
        content = file.file.read()
        data_file.write(content)

        # group = df.groupby('Location').size()
        # grouped = pd.DataFrame({'Location': group.index, 'Count': group.values})
        # grouped_data = grouped.to_dict('records')
        # return {"message": f"Total length of file is {file_len}"}
        # return templates.TemplateResponse(request=request, name="file.html", context={"file_size": file_len, 'grouped_data':grouped_data})
        # return templates.TemplateResponse(request=request, name="file.html", context={"file_size": file_len})
        return {'message': f'File uploaded'}
    except Exception as e:
        print(e)
        return {"Error": e}

@app.post("/send-notification/{email}")
async def send_notification(email: str):
    with open("log.txt", mode="w") as email_file:
        message = "some notification"
        content = f"notification for {email}: {message}"
        email_file.write(content)
    return {"message": "Notification sent in the background"}

if __name__ == "__main__":
    uvicorn.run(app,port=7000)

