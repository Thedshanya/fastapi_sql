from fastapi import FastAPI
from src.routes.sign_in import user


app=FastAPI()


app.include_router(user.routes)



    

















