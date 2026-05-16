from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory DB
items = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 800},
]

# Request body model
class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def home():
    return {"message": "FastAPI running"}

# GET all items
@app.get("/items")
def list_items():
    return {"items": items}

# POST create item
@app.post("/items")
def create_item(item: Item):
    new_item = {
        "id": len(items) + 1,
        "name": item.name,
        "price": item.price
    }

    items.append(new_item)

    return {
        "message": "Item created",
        "item": new_item
    }
