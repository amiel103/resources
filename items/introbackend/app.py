from sqlmodel import Session , select

from database import create_db_and_tables, engine
from models import Employee  ,department



def main():
    create_db_and_tables()
    # what you want to do here

if __name__ == "__main__":
    main()