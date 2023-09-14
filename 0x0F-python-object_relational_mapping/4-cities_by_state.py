#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


def cities_by_states():
    """ lists all cities from the database hbtn_0e_4_usa"""
    datab = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = datab.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id=states.id"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    datab.close()


if __name__ == "__main__":
    cities_by_states()
