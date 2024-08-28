from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(50),unique=True)
    email = Column(String(50))
    password = Column(String(50))

# class Post(Base):
#     __tablename__ = 'posts'

#     id = Column(Integer,primary_key=True,index=True)
