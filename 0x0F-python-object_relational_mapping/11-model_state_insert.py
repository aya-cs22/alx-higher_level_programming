#!/usr/bin/python3
"""a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_object = State(name="Louisiana")
    state = session.add(new_object)
    session.commit()
    print(f'{new_object.id}')
    session.close()
