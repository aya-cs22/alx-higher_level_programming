#!/usr/bin/python3
"""this module an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_access = MySQLdb.connect(port=3306, host="localhost",
                                user=argv[1], passwd=argv[2], db=argv[3])
    cur = db_access.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY='{}'".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_access.close()
