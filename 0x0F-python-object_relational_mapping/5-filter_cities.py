#!/usr/bin/python3
"""a script that lists all cities
    from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

def city_list():
    """list ciy"""
    database = MySQLdb.connect(host="localhost",user=sys.argv[1], passwd=sys.argv[2],db=sys.argv[3], port=3306)
    c = database.cursor()
    state_name = sys.argv[4]
    query = "SELECT  cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE %s ORDER BY cities.id ASC" 
    c.execute(query, (f'%{state_name}%',))
    rows = c.fetchall()
    re = ""
    for row in rows:
        re += row[0] + ", "
    print(re[0:-2:])
    c.close()
    database.close()


if __name__ == "__main__":
    city_list()
