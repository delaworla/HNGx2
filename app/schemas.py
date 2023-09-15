from pydantic import BaseModel
from datetime import datetime
from pytz import timezone


class Person(BaseModel):
    name: str


class CreatePerson(BaseModel):
    name: str


class UpdatePerson(BaseModel):
    name: str

def get_current_time():
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

class CreateResponse(BaseModel):
    name: str
    created_at: str = get_current_time()
    
class UpdateResponse(BaseModel):
    name: str
    last_modified: str = get_current_time()
