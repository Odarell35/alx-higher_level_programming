#!/usr/bin/python3
"""a script that lists all cities
    from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

def city_list():
    """list ciy"""
    database = MySQLdb.connect(host="localhost",user=sys.argv[1], passwd=sys.argv[2],db=sys.argv[3], port=3306)
    c = database.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id  ORDER BY cities.id ASC"
    c.execute(query)
    row = c.fetchall()
    for rr in row:
        print(rr)
    c.close()
    database.close()


if __name__ == "__main__":
    city_list()
