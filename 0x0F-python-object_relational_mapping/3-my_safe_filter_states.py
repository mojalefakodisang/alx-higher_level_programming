#!/usr/bin/python3
"""Displays all values with state_name in argument"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    USER = sys.argv[1]
    PWD = sys.argv[2]
    DB_NAME = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(user=USER, passwd=PWD, db=DB_NAME)
    cur = db.cursor()
    cur.execute("""SELECT id, name
                FROM states
                WHERE BINARY name = %s
                ORDER BY id""", (state_name,))
    all = cur.fetchall()
    for i in all:
        print(i)
