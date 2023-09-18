from datetime import datetime 
from pydantic import BaseModel

class Person(BaseModel):
    name: str


class Response(BaseModel):
    id:int
    name: str 
    created_at: datetime
    class Config:
        orm_mode = True
    
class UpdateResponse(Response):
    last_modified: datetime
    
    class Config:
        orm_mode = True
        