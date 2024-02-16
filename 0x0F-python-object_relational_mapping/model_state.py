#!/usr/bin/python3
"""
State class and Base, an instance of declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData

Metadata = MetaData()
Base = declarative_base(metadata=Metadata)


class State(Base):
    """
    Class of id and name attributes of states
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
