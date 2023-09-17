#!/usr/bin/python3
"""Module to list State"""
import MySQLdb
import sys


def list_states():
    """lists state names"""
    datab = MySQLdb.connect(host='localhost',
                            port=3306,
                            user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3],
                            charset="ut8")
    cur = datab.cursor()
    query = "SELECT id, name FROM states ORDER by id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    datab.close()


if __name__ == "__main__":
    list_states()
