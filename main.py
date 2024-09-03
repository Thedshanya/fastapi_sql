from fastapi import FastAPI
from src.routes.sign_in import user
from src.routes.hospital import route
from src.config.database import Base,engine
# from src.routes.sign_in.models import User, Hospital




app=FastAPI()

Base.metadata.create_all(bind=engine)



app.include_router(user.rout)
app.include_router(route.route)




    

















