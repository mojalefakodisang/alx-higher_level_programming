#!/usr/bin/python3
"""Displays cities with their states"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    USER = sys.argv[1]
    PWD = sys.argv[2]
    DB_NAME = sys.argv[3]
    db = MySQLdb.connect(user=USER, passwd=PWD, db=DB_NAME)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities JOIN states
                ON state_id = states.id
                ORDER BY cities.id ASC""")
    all = cur.fetchall()
    for i in all:
        print(i)
