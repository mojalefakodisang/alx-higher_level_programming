#!/usr/bin/python3
"""Model that creates a City table"""
from model_state import State, Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """Class that declares a new city"""
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
