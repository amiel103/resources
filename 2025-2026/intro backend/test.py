from sqlmodel import SQLModel, create_engine 

connection_string = "sqlite:///database.db"
engine = create_engine( connection_string )

from sqlmodel import Field, SQLModel

class Employee(SQLModel, table=True):
    empid: int | None = Field(default=None, primary_key=True)
    name: str
    dept: int | None = Field(default=None, foreign_key="department.id")
    age: int | None = None

class Department(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

from sqlmodel import Session, select

with Session(engine) as session:
    with Session(engine) as session:
        statement = select(Employee, Department).join(Department).where(Department.name == "IT")
        results = session.exec(statement)
        for x in results:
            print(x)









 

        





SQLModel.metadata.create_all(engine)
