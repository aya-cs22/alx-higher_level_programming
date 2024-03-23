#!/usr/bin/python3
""" arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_access = MySQLdb.connect(port=3306, host="localhost",
                                user=argv[1], passwd=argv[2], db=argv[3])
    cur = db_access.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_access.close()
