from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os
import const
app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float
    tax: float

@app.get("/items/", response_model=List[Item])
def read_items():
    return [
        {
            "id": 1,
            "name": os.getenv('user1', 'dummy user1'),
            "description": const.desc1,
            "price": 10.5,
            "tax": 1.5
        },
        {
            "id": 2,
            "name": os.getenv('user2', 'dummy user2'),
            "description": const.desc2,
            "price": 20.0,
            "tax": 2.0
        }
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
