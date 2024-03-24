#!/usr/bin/python3
"""a script that prints the first State object from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}@localhost/{}'.format(sys.argv[1], sys.argv[2]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
states = session.query(State).first()
if not states:
    print("Nothing")
else:
    for state in states:
        print(f'{state.id}: {state.name}')
session.close()
