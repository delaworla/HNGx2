from pydantic import BaseModel


class Person(BaseModel):
    name: str

    

class CreatePerson(BaseModel):
    name: str

    
class UpdatePerson(BaseModel):
    name: str