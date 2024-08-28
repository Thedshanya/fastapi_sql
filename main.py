from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing_extensions import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()
models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    name:str
    email:str
    password:str

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/users/",status_code=status.HTTP_201_CREATED)
async def create_user(user:UserBase, db:db_dependency):
    db_user = models.User(**user.model_dump()) 
    db.add(db_user)
    db.commit()

@app.get("/users/{user_id}",status_code=status.HTTP_200_OK)
async def read_user(user_id:int, db:db_dependency):
    user = db.query(models.User).filter(models.User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user
@app.delete("/users/{user_id}",status_code=status.HTTP_200_OK)
async def delete_user(user_id:int,db:db_dependency):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404,detail='User not found')
    db.delete(db_user)
    db.commit()

@app.put("/users/{user_id}",status_code=status.HTTP_200_OK)
async def update_use(user_id:int,up_user:UserBase,db:db_dependency):
    user=db.query(models.User).filter(models.User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail='User not found')
    user.name=up_user.name
    user.email=up_user.email
    user.password=up_user.password
    db.commit()













