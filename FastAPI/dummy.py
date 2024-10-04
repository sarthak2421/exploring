items = {
    'item1':{"id":1,"name": "Apple", "desc": "The red fruit", "price": 62, "tax": 5},
    'item2':{"id":2,"name": "Orange", "price": 50, "tax": 3},
    'item3':{"id":3,"name": "Banana", "desc": "The yellow fruit", "price": 45}
}
print(items)
i = items['item1']['name']
dict1 =  {'Item name':f'{i}'}

print(dict1)
# --------------------------------------------------------
# main.py
from fastapi import FastAPI, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/", response_class=HTMLResponse)
def read_form():
    return """
    <html>
        <body>
            <form action="/items/" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name"><br><br>
                <label for="description">Description:</label>
                <input type="text" id="description" name="description"><br><br>
                <label for="price">Price:</label>
                <input type="text" id="price" name="price"><br><br>
                <label for="tax">Tax (optional):</label>
                <input type="text" id="tax" name="tax"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """

@app.post("/items/")
async def create_item_from_form(name: str = Form(...), description: str = Form(...), price: float = Form(...), tax: float = Form(None)):
    item = Item(name=name, description=description, price=price, tax=tax)
    return item










# main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import List
import shutil

app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    # Save the uploaded file to a local directory
    with open(f"uploaded_files/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...)):
    # Save each uploaded file to a local directory
    for file in files:
        with open(f"uploaded_files/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    return {"filenames": [file.filename for file in files]}

@app.get("/", response_class=HTMLResponse)
def read_form():
    return """
    <html>
        <body>
            <form action="/uploadfile/" method="post" enctype="multipart/form-data">
                <label for="file">Choose a file:</label>
                <input type="file" id="file" name="file"><br><br>
                <input type="submit" value="Upload File">
            </form>

            <form action="/uploadfiles/" method="post" enctype="multipart/form-data">
                <label for="files">Choose multiple files:</label>
                <input type="file" id="files" name="files" multiple><br><br>
                <input type="submit" value="Upload Files">
            </form>
        </body>
    </html>
    """


