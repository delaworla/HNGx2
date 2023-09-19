from datetime import datetime 
from pydantic import BaseModel

class Person(BaseModel):
    name: str

class Update(BaseModel):
    name: str 
    last_modified: datetime
class Response(BaseModel):
    id: int
    name: str 
    created_at: datetime
   
    class Config:
        orm_mode = True


