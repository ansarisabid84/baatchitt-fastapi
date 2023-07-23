# main.py

from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Route for the root URL
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Route for another endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
