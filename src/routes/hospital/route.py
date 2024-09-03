from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import HTTPException,status
from ...routes import models
from ...routes.models import db_dependency as db_dependency


route=APIRouter()


app=APIRouter()

class HospitalBase(BaseModel):
    name : str
    address : str
    phone : str
    doctors : int
    nurses: int
    bed_available: int


#Add hospital
@route.post("/add_hospital",status_code=status.HTTP_201_CREATED)
async def add_hospital(user:HospitalBase, db:db_dependency):
    db_hos = models.Hospital(**user.model_dump()) 
    db.add(db_hos)
    db.commit()

#retrieve a hospital
@route.get("/hospital/{hos_id}",status_code=status.HTTP_200_OK)
async def retrieve_hospital(hos_id:int, db:db_dependency):
    hospital = db.query(models.Hospital).filter(models.Hospital.id==hos_id).first()
    if hospital is None:
        raise HTTPException(status_code=404, detail='User not found')
    return hospital

#Retrieve all Hospital
@route.get("/hospital",status_code=status.HTTP_200_OK)
async def retrieve_all_hospital(db:db_dependency):
    hospital=db.query(models.Hospital).all()
    # for hos in db.query(models.Hospital).all:
    #     hospital+=hos
    # hospital = db.query(models.Hospital).filter(models.Hospital.id==hos_id).first()
    # if hospital is None:
    #     raise HTTPException(status_code=404, detail='User not found')
    return hospital

#Update hospital
@route.put("/hospital/{hos_id}",status_code=status.HTTP_200_OK)
async def update_hospital(hos_id:int,hos_user:HospitalBase,db:db_dependency):
    hospital=db.query(models.Hospital).filter(models.Hospital.id==hos_id).first()
    if hospital is None:
        raise HTTPException(status_code=404,detail='User not found')
    hospital.name=hos_user.name
    hospital.address=hos_user.address
    hospital.phone=hos_user.phone
    hospital.doctors=hos_user.doctors
    hospital.nurses=hos_user.nurses
    hospital.bed_available=hos_user.bed_available
    db.commit()

#Delete Hospital
@route.delete("/hospital/{hospital_id}",status_code=status.HTTP_200_OK)
async def delete_hospital(hos_id:int,db:db_dependency):
    db_hos = db.query(models.Hospital).filter(models.Hospital.id == hos_id).first()
    if db_hos is None:
        raise HTTPException(status_code=404,detail='User not found')
    db.delete(db_hos)
    db.commit()


