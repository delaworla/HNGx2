from datetime import datetime 
from pydantic import BaseModel

class Person(BaseModel):
    name: str


class Response(Person):
    id: int
    created_at: datetime
   
    class Config:
        orm_mode = True


