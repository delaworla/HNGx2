from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


class Persons(Base):
    __tablename__ ="persons"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    last_modified=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))