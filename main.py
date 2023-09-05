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


def find_person(id):
    for p in my_people:
        if p['id'] == id:
            return p


@app.get("/api/person/{id}")
async def read_person(id: int):
    person = find_person(id)
    return {"data": person}
