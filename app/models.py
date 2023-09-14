from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import null


class Persons(Base):
    __tablename__ ="persons"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer,nullable=False)