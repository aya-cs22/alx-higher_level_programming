#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Column, Integer, String

from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

class State(Base):
    """creat table State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), primary_key=False)
Base.metadata.create_all(engine)
