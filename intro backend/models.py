from sqlmodel import Field , SQLModel

class Employee(SQLModel, table=True):
    empid: int | None = Field(default=None, primary_key=True)
    name: str
    dept: int | None = Field(default=None, foreign_key="department.id")
    age: int | None = None

class Department(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str