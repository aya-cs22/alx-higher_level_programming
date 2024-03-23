#!/usr/bin/python3
""" this module connect the database with python using argv
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    port = "3306"
    host = "localhost"
    db_access = MySQLdb.connect(host=host, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db_access.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        for col in row:
            print ("%s," % col)
    cur.close()
    db_access.close()
