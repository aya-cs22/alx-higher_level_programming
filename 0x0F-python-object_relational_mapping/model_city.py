#!/usr/bin/python3
"""Start link class to table in database """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from model_state import Base
Base = declarative_base()


class City(Base):
    """creat table City"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey=True, nullable=False)
