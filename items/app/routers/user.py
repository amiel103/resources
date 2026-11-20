from fastapi import APIRouter
from app.models import Users
from sqlmodel import Session, select

router = APIRouter(prefix="/users", tags=["users"])
from app.database import engine

@router.get("/", summary="users")
async def get_all():
    with Session(engine) as session:
        statement = select( Users)
        results = session.exec(statement).all()
        return results


@router.get("/{id}")
async def read_employee(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        user = session.get(Users, id)
        return {"message": user}
    

@router.post("/")
async def root(users  : Users):
    with Session(engine) as session:
        session.add(users)
        session.commit()
        session.refresh(users)
        return {"message": users}
    
@router.post("/login")
async def root(users  : Users):
    with Session(engine) as session:

        statement = select(Users).where(Users.name == users.name).where(Users.password == users.password)
        results = session.exec(statement)

        result = results.first()
        print(result)

        if (result == None):
            return {"status":"failed"}


        return {
            "status":"success",
            "data": result
            }
    