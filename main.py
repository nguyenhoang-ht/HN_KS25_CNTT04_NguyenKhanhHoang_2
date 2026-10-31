from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import engine,SessionLocal
import models
import schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def test():
    print("run")

@app.get("/device/")
def get_device():
    pass

@app.post("/")
def new_device():
    pass

@app.delete("/")
def delete_device():
    pass