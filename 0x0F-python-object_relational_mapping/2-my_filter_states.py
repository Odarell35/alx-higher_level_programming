#!/usr/bin/python3
"""Module to filter States"""
import MySQLdb
import sys

def user_input():
    """Lists state names that are searched"""
    if len(sys.argv) < 5:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name> <name_search>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    name_search = sys.argv[4]

    try:
        datab = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database_name,
            charset="utf8"
        )

        cur = datab.cursor()

        # Use %s as a placeholder for the name_search parameter
        query = "SELECT id, name FROM states WHERE name LIKE %s ORDER by id ASC"
        cur.execute(query, (f'%{name_search}%',))

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        datab.close()

    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    user_input()

