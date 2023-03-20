#!/usr/bin/python3
""" module that contains the class definition of a State
    and an instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ class State

        Args:
            Base (Object): Base class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
