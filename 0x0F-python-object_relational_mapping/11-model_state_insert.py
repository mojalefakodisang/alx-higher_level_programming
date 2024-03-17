#!/usr/bin/python3
"""Adds a new state into the database"""
import sys
from model_state import State, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.\
        format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
