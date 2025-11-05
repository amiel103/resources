from sqlmodel import Session , select

from database import create_db_and_tables, engine
from models import Employee , Department

def create_employee( _name, _dept ):
    with Session(engine) as session:
        emp = Employee( name = _name , dept = _dept )
        session.add(emp)
        session.commit()


def create_department(  _name ):
    with Session(engine) as session:
        emp = Department( name =  _name )
        session.add(emp)
        session.commit()
        


def main():
    create_db_and_tables()
    create_employee(  'Kurt Cobain' ,  1 )
    create_department(  'Cleaning'  )

if __name__ == "__main__":
    main()
