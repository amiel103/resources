from sqlmodel import Session , select

from database import create_db_and_tables, engine
from models import Employee  ,department



def main():
    create_db_and_tables()
    # what you want to do here

    
    emp1 = Employee(  name='Clark', dept='Sales')
    emp2 = Employee(  name='Dave', dept='Accounting')
    emp3 = Employee(  name='Ava', dept='Sales')

    with Session(engine) as session:
        session.add(emp1)
        session.add(emp2)
        session.add(emp3)
        session.commit()


if __name__ == "__main__":
    main()