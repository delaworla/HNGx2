from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: str
    

class CreatePerson(BaseModel):
    name: str
    age: str
    
class UpdatePerson(BaseModel):
    name: str
    age: str