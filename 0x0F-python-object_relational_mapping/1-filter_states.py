#!/usr/bin/python3
"""Lists all staes with name starting with N"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    USER = sys.argv[1]
    PWD = sys.argv[2]
    DB_NAME = sys.argv[3]
    db = MySQLdb.connect(user=USER, passwd=PWD, db=DB_NAME)

    cur = db.cursor()
    cur.execute("""SELECT id, name
                FROM states
                WHERE BINARY name LIKE %s
                ORDER BY id""", ('N%',))
    all = cur.fetchall()
    for i in all:
        print(i)
