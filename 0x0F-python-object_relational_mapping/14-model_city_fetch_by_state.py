#!/usr/bin/python3
""" a Python file similar to model_state.py named model_city.py
that contains the class definition of a City."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).filter(City.state_id == State.id)
    for city, state in cities:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.commit()
    session.close()
