from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add")
def read_item(number: int, number_add: Union[int, None] = None):
    if number_add:
        number += number_add
    else:
        number += 10
    return {"result": number}

@app.post("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price": item.price}