from fastapi import FastAPI, status, HTTPException, Response, Depends
import psycopg2
from typing import Dict
import time
from psycopg2.extras import RealDictCursor
from sqlalchemy import asc
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.get("/")
def get_persons(db:Session =Depends(get_db)):
    persons = db.query(models.Persons).order_by(asc(models.Persons.id)).all()
    return persons


@app.post("/api", status_code=status.HTTP_201_CREATED)
async def create_person(persons: schemas.Person, db:Session =Depends(get_db)):
    person = models.Persons(name=persons.name.lower())
    db.add(person)
    db.commit()
    db.refresh(person)
    return person
    




@app.get("/api/{user_id}")
async def read_person(user_id, db:Session =Depends(get_db)):
    if user_id.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user_id)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user_id.lower()).first()
    if not person:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"person with id: {user_id} was not found")
    return  person





@app.delete("/api/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_person(user_id, db:Session =Depends(get_db)):
    if user_id.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user_id)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user_id.lower()).first()
    if not person:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"person with id: {user_id} was not found")
    if not person:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {user_id} does not exist")
    db.delete(person)
    db.commit()
    
    return  person
    
    
    # deleted_person = db.query(models.Persons).filter(models.Persons.id == user_id)
    # if deleted_person.first() == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"post with id: {user_id} does not exist")
    # deleted_person.delete(synchronize_session=False)
    # db.commit()
    # return Response(status_code=status.HTTP_204_NO_CONTENT)



@app.put("/api/{user_id}")
async def update_person(user_id, persons: schemas.UpdatePerson, db:Session =Depends(get_db)):
    if user_id.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user_id)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user_id.lower()).first()
    if not person:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"person with id: {user_id} was not found")
    person = person.name.lower()
    db.commit()
    return  person
   
    # update_person = db.query(models.Persons).filter(models.Persons.id == user_id) 
    # updated_person= update_person.first()
    # if updated_person == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"post with id: {user_id} does not exist")
    # update_person.update(person.dict(), synchronize_session=False)
    # db.commit()
    # return update_person.first()
