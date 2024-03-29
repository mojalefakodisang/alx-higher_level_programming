#!/usr/bin/python3
"""Fetch all states"""
import sys
from model_state import State
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
    states = session.query(State).all()

    for i in states:
        print("{}: {}".format(i.id, i.name))

    session.close()
