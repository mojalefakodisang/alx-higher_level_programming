#!/usr/bin/python3
"""Displays all City objects from the database hbtn_0e_14_usa"""
import sys
from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ), pool_pre_ping=True)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    all_rows = session.query(City, State).join(State).all()

    for i in all_rows:
        print("{}: ({}) {}".format(i.State.name, i.City.id, i.City.name))
    session.close()
