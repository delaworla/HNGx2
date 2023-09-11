from fastapi import fastapi, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

db: Dict[int, dict] = {}

class Person(BaseModel):
    name: str
    age: str 
    email: str

@app.post("/api/person/", response_model=Person)
    