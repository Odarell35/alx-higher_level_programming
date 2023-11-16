#!/usr/bin/python3
"""a script that lists all states
    from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def state_name():
    """list states"""
    database = MySQLdb.connect(host="localhost",
                               user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3],
                               port=3306)
    c = database.cursor()
    name_search = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC"
    c.execute(query, (f'%{name_search}%',))
    row = c.fetchall()
    for rr in row:
        print(rr)
    c.close()
    database.close()


if __name__ == "__main__":
    state_name()
