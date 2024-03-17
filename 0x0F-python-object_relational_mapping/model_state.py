#!/usr/bin/python3
"""Module that creates a State table"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """Class that declares a new state"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
