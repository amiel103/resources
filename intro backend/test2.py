from fastapi import FastAPI
from sqlmodel import Session, select

from fastapi import APIRouter, HTTPException , status


from models import Employee
from database import create_db_and_tables , engine

from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)



# get all employee endpoint

@app.get("/employee")
async def read_employee():
    with Session(engine) as session:
        statement = select(Employee)
        results = session.exec(statement).all()
        return results

# get specific employee endpoint
@app.get("/employee/{id}")
async def read_employee(id):
    with Session(engine) as session:
        emp = session.get(Employee, id)
        return {"message": emp}

# create employee endpoint
@app.post("/employee")
async def root(employee : Employee):
    with Session(engine) as session:
        session.add(employee)
        session.commit()
        session.refresh(employee)

        return f"employee {employee.name} created"


# update specific employee endpoint
@app.put("/employee/{item_id}")
async def root( item_id:int , employee : Employee):
    print(id, '---------------------------')
    with Session(engine) as session:
        item = session.get(Employee, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Users not found")

        item.name = employee.name
        session.add(item)
        session.commit()
        session.refresh(item)

        return f"{item_id} updated"


# update specific employee endpoint
@app.delete("/employee/{item_id}")
async def root( item_id:int , employee : Employee):
    print(id, '---------------------------')
    with Session(engine) as session:
        item = session.get(Employee, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Users not found")

        session.delete(item)
        session.commit()

        return f"{item_id} deleted"


@app.get("/Welcome")
async def root():
    return {"message": "Hello World"}

@app.get("/")
async def root():
    return {"message": "Hello DS"}



