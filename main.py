from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from random import randrange

app = FastAPI()


class Person(BaseModel):
    name: str
    age: str
    email: str


my_people = [{"name": "Emma", "age": "23", "email": "emma@hngx.com",
              "id": 1}, {"name": "Sam", "age": "23", "email": "sam@hngx.com", "id": 2}]


@app.get("/api/persons")
def get_persons():
    return {"data": my_people}


@app.post("/api/person/")
async def create_person(person: Person):
    person_dict = person.dict()
    person_dict['id'] = randrange(0, 10000000)
    my_people.append(person_dict)
    return {"data": person_dict}


@app.get("/api/person/{person_id}")
async def read_person(id: int):
    if id not in my_people:
        raise HTTPException(status_code=404, detail="Person not found")
    return {"data": f"Here is person {'id'}"}
