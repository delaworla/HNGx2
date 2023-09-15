from pydantic import BaseModel
from datetime import datetime
from pytz import timezone


class Person(BaseModel):
    name: str


class CreatePerson(BaseModel):
    name: str


class UpdatePerson(BaseModel):
    name: str

current_time_utc = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

class Response(BaseModel):
    name: str
    created_at: str = current_time_utc
    
class UpdateResponse(BaseModel):
    name: str
    last_modified: str
    
    class Config:
        orm_mode = True
        