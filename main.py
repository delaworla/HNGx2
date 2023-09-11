from fastapi import fastapi, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

db: Dict[int, dict] = {}
