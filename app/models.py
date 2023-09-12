from .database import Base
from sqlalchemy import Column, Integer, String


class Persons(Base):
    __tabelename__ ="persons"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)