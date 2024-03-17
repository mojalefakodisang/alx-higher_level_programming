#!/usr/bin/python3
"""Displays cities by their states"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    USER = sys.argv[1]
    PWD = sys.argv[2]
    DB_NAME = sys.argv[3]
    db = MySQLdb.connect(user=USER, passwd=PWD, db=DB_NAME)
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities JOIN states
                ON state_id = states.id
                WHERE BINARY states.name = %s
                ORDER BY cities.id ASC""", (sys.argv[4], ))
    all = cur.fetchall()
    all_len = len(all)
    for i in range(all_len):
        if i == all_len - 1:
            print(all[i][0], end='')
        else:
            print(all[i][0], end=", ")
    print()
