#!/usr/bin/python3
"""this module lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
from sys import argv
if __name__ == "__main__":
    db_access = MySQLdb.connect(port=3306, host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db_access.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_access.close()
