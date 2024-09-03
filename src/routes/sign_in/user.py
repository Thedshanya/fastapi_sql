
from fastapi import HTTPException,status,APIRouter
from pydantic import BaseModel
# from sqlalchemy.orm import Session
# from typing_extensions import Annotated
# from src.config.database import engine
# from src.util.db_dependency import get_db

from ...routes import models


rout=APIRouter()



# models.Base.metadata.create_all(bind=engine)



class UserBase(BaseModel):
    name:str
    email:str
    password:str
    role:str
class UserLogin(BaseModel):
    email:str
    password:str
    role:str



# db_dependency = Annotated[Session, Depends(get_db)]



@rout.post("/signup",status_code=status.HTTP_201_CREATED)
async def create_user(user:UserBase, db:models.db_dependency):
    db_user = models.User(**user.model_dump()) 
    db.add(db_user)
    db.commit()

@rout.post("/signin",status_code=status.HTTP_202_ACCEPTED)
async def check_user(user:UserLogin, db:models.db_dependency):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user and db_user.password == user.password and db_user.role == user.role:
        return {"msg":"sigin successful"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    