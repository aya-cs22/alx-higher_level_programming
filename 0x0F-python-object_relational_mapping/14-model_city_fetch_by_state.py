#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from sqlalchemy import (create_engine)
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).filter(City.state_id == State.id)
    for city, state in cities:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
