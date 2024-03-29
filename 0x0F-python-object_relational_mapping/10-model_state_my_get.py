#!/usr/bin/python3
"""Fetch a state from arguments"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ), pool_pre_ping=True)

    '''Make a session'''
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == sys.argv[4])

    if state.count() > 0:
        for i in state:
            print(i.id)
    else:
        print("Not found")

    session.close()
