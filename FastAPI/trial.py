from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Annotated

class Item(BaseModel):
    name:str
    desc:str | None=None
    price:float
    tax:float | None=None

app = FastAPI()

@app.get('/users/me')
async def root_user():
    return {"Message":"Current User!!"}

@app.get('/users/{uid}')
async def read_user(uid:str):
    return {"Message":f"User ID = {uid}"}

'''Query parameters'''
@app.get('/items/{item_id}')
async def read_item(item_id:str, q:str | None=None, short:bool=False):
    if q:
        return {"item_id": item_id, "q": q}
    if not short:
        return {"desc":"Not too long!"}
    return {"item_id": item_id}

'''Post method'''
@app.post('/createItems/')
async def create_item(item:Item):
    return item


'''String Validation'''
@app.get('/valid')
async def valid(q:Annotated[str | None, Query(max_length=5)]="fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''Int validation with path'''
@app.get('/intValid/{intid}')
async def intValid(intid:Annotated[int | None,Path(title='ID', ge=1)]=None, q:Annotated[str | None, Query(min_length=3)]=None):
    results = {"item_id": intid}
    if q:
        results.update({"q": q})
    return results

