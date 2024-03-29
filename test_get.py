import imp
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name:str
    price:float
    is_offer:Optional[bool]=None



@app.get("/")
def read_root():
    return {"hello" : "hihi"}

@app.get("/items/{item_id}")
def read_items(item_id: int, q:Optional[str]=None):
    return {"item_id":item_id, "q":q}

@app.put("/items/{item_id}")
def update_items(item_id: int, item:Item):
    return { "item_name":item.name,"item_id":item_id }