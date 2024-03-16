#!/usr/bin/env python3
from sqlalchemy import create_engine, MetaData, Table
import sys

db_uri = f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}'
engine = create_engine(db_uri)
connection = engine.connect()
metadata = MetaData()
metadata.reflect(bind=engine)

states_table = Table('states', metadata, autoload=True)
results = connection.execute(states_table.select().order_by(states_table.c.id.asc()))

rows = results.fetchall()
for row in rows:
  print(row)
  
connection.close()