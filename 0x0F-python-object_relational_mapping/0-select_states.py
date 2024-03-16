#!/usr/bin/python3
"""Select the states table"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    USER = sys.argv[1]
    PWD = sys.argv[2]
    DB_NAME = sys.argv[3]
    db = MySQLdb.connect(user=USER, passwd=PWD, db=DB_NAME)
    cur = db.cursor()
    cur.execute('SELECT id, name FROM states ORDER BY id')
    all = cur.fetchall()
    for i in all:
        print(i)
