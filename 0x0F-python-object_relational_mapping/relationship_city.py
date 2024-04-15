#!/usr/bin/python3
"""Start link class to table in database """
from sqlalchemy import Integer, Column, String, ForeignKey
from relationship_state import Base


class City(Base):
    """creat table City"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
