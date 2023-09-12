from .database import Base
from sqlalchemy import Column, Integer, String


class Persons(Base):
    __tabelename__ ="persons"
    