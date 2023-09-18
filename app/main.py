from fastapi import FastAPI, status, HTTPException, Depends
import pydantic
from sqlalchemy import asc
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.get("/api")
def get_persons(db:Session =Depends(get_db)):
    persons = db.query(models.Persons).order_by(asc(models.Persons.id)).all()
    return persons


@app.post("/api", status_code=status.HTTP_201_CREATED, response_model=schemas.Response)
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
    db.delete(person)
    db.commit()
    
    return  person


@app.put("/api/{user_id}", response_model=schemas.UpdateResponse)
async def update_person(user_id, persons: schemas.Person, db:Session =Depends(get_db)):
    if user_id.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user_id)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user_id.lower()).first()
    if not person:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"person with id: {user_id} was not found")
    person.name = persons.name.lower()
    db.commit()
    current_time_utc = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    
    return person.name
