from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel
from typing import Dict
from random import randrange
from starlette import status
import requests
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Person(BaseModel):
    name: str
    age: str
    


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='HNGx', user='postgres',
                                password='postgres', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database was connected successfully")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error:", error)
        time.sleep(2)


my_people = [{"name": "Emma", "age": "23", "email": "emma@hngx.com",
              "id": 1}, {"name": "Sam", "age": "23", "email": "sam@hngx.com", "id": 2}]


@app.get("/api/persons")
def get_persons():
    cursor.execute("""SELECT * FROM persons""")
    peoples = cursor.fetchall()
    return {"data": peoples}


@app.post("/api/person/", status_code=status.HTTP_201_CREATED)
async def create_person(person: Person):
    cursor.execute(""" INSERT INTO persons(name,age) VALUES(%s,%s) RETURNING *""", (person.name, person.age))
    new_people =cursor.fetchone()
    conn.commit()
    return {"data": new_people}
    


def find_person(id):
    for p in my_people:
        if p['id'] == id:
            return p


@app.get("/api/person/{id}")
async def read_person(id: int):
    cursor.execute(""" SELECT * FROM persons WHERE id = %s""",(str(id)))
    person = cursor.fetchone()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"person with id: {id} was not found")
    return {"data": person}


def find_index_person(id):
    for i, p in enumerate(my_people):
        if p['id'] == id:
            return i


@app.delete("/api/person/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_person(id: int):
    cursor.execute(""" DELETE FROM persons WHERE id = %s RETURNING * """ ,(str(id),))
    deleted_person = cursor.fetchone()
    conn.commit()
    if deleted_person == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/api/person/{id}")
async def update_person(id: int, person: Person):
    cursor.execute((""" UPDATE persons SET name=%s, age=%s WHERE id = %s RETURNING * """),(person.name, person.age, str(id)))
    updated_person = cursor.fetchone()
    conn.commit()
    if updated_person == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
   
    return {"message": updated_person}
