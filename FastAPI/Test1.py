from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import uvicorn
app = FastAPI()

class Item(BaseModel):
    name: str
    desc: str | None=None
    price: int
    tax: int| None=None

items = {
    'item1':{"name": "Apple", "desc": "The red fruit", "price": 62, "tax": 5},
    'item2':{"name": "Orange", "price": 50, "tax": 3},
    'item3':{"name": "Banana", "desc": "The yellow fruit", "price": 45}
}

@app.get('/')
async def home():
    return {'Message':'Home Page'}

@app.post('/createItems/')
async def createItem(item : Item):
    items['item4']=jsonable_encoder(item)
    print(items)
    return item

@app.get('/item/{item}')
async def item(item:str):
    if item not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    # return {'Item Name': f'{itemid}'}
    return items[item]

@app.put('/item/{item}', response_model=Item)
async def update(item:str, itemobj:Item):
    if item not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = jsonable_encoder(itemobj)
    print(updated)
    items[item] = updated
    print(items)
    return updated


