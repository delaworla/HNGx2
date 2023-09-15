from fastapi import FastAPI, status, HTTPException, Response, Depends
import psycopg2
from typing import Dict
import time
from psycopg2.extras import RealDictCursor
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()



my_people = [{"name": "Emma", "age": "23", "email": "emma@hngx.com",
              "id": 1}, {"name": "Sam", "age": "23", "email": "sam@hngx.com", "id": 2}]


@app.get("/")
def get_persons(db:Session =Depends(get_db)):
    persons = db.query(models.Persons).all()
    return {"data": persons}


@app.post("/api", status_code=status.HTTP_201_CREATED)
async def create_person(person: schemas.Person, db:Session =Depends(get_db)):
    
    created_person = models.Persons(**person.dict())
    db.add(created_person)
    db.commit()
    db.refresh(created_person)
    return {"data": created_person}
    




@app.get("/api/user_id")
async def read_person(id: int, db:Session =Depends(get_db)):
   person = db.query(models.Persons).filter(models.Persons.id == id).first()   
   if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"person with id: {id} was not found")
   return {"data": person}





@app.delete("/api/user_id", status_code=status.HTTP_204_NO_CONTENT)
async def delete_person(id: int, db:Session =Depends(get_db)):
    deleted_person = db.query(models.Persons).filter(models.Persons.id == id)
    if deleted_person.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    deleted_person.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@app.put("/api/user_id")
async def update_person(id: int, person: schemas.Person, db:Session =Depends(get_db)):
    update_person = db.query(models.Persons).filter(models.Persons.id == id) 
    updated_person= update_person.first()
    if updated_person == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    update_person.update(person.dict(), synchronize_session=False)
    db.commit()
    return {"message": update_person.first()}
