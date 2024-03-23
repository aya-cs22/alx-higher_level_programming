#!/usr/bin/python3
""" in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_access = MySQLdb.connect(port=3306, host="localhost",
                                user=argv[1], passwd=argv[2], db=argv[3])
    cur = db_access.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                WHERE states.name=%s
                ORDER BY cities.id ASC;""", (argv[4],))
    rows = cur.fetchall()
    first = True
    for row in rows:
        for coulmn in row:
            if not first:
                print(", ",end="")
            print(coulmn, end="")
        city_id, city_name, state_name = row
        print(city_name)
    cur.close()
    db_access.close()
