#!/usr/bin/python3
"""Updates state name with ID 2"""
import sys
from model_state import State, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))
    states.delete()
    session.commit()
    session.close()
