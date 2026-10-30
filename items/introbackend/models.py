from sqlmodel import Field , SQLModel

class Employee(SQLModel, table=True):
    empid: int | None = Field(default=None, primary_key=True)
    name: str
    dept: str
    age: int | None = None

class department(SQLModel, table=True):
    empid: int | None = Field(default=None, primary_key=True)
    name: str
    dept: str
    age: int | None = None