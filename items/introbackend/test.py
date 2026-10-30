from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine

from models import Employee 

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/employee/{id}")
async def read_employee(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        emp = session.get(Employee, id)
        return {"message": emp}
    

@app.post("/employee")
async def root(employee  : Employee):
    with Session(engine) as session:
        session.add(employee)
        session.commit()
        session.refresh(employee)

        return {"message": 'created'}