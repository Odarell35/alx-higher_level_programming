#!/usr/bin/python3
"""Module to filters States"""
import MySQLdb
import sys


def filter_states():
    """lists state names that start with N"""
    datab = MySQLdb.connect(host='localhost', port=3306,
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], charset="utf8" )
    cur = datab.cursor()
    query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER by id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    datab.close()


if __name__ == "__main__":
    filter_states()
