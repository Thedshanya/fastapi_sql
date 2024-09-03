from sqlalchemy import Column, Integer, String
from src.config.database import Base
from fastapi import Depends
from sqlalchemy.orm import Session
from typing_extensions import Annotated
from src.util.db_dependency import get_db


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(50),unique=True)
    email = Column(String(50))
    password = Column(String(50))
    role=Column(String(50))

class Hospital(Base):
    __tablename__  = 'hospitals'

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(50),unique=True)
    address = Column(String(100))
    phone = Column(String(15))
    doctors = Column(Integer)
    nurses=Column(Integer)
    bed_available=Column(Integer)

# Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]



