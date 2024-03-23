#!/usr/bin/python3
"""this module lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
from sys import argv
if __name__ == "__main__":
    port = "3306"
    host = "localhost"
    db_access = MySQLdb.connect(username = argv[1], passwd = argv[2], db = argv[3])
    cur = db_access.cursor()
    cur.excute("SELECT * FROM statesn ORDER BY states.id ASC")
    rows = cur.ferchall()
    for row in rows:
        print(row)
    cur.close()
    db_access.close()
