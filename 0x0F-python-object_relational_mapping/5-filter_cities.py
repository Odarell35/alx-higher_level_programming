#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


def cities_by_states():
    """ lists all cities from the database hbtn_0e_4_usa"""
    datab = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    state_n = sys.argv[4]
    cur = datab.cursor()
    cur.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (state_n,))
 #   query = "SELECT  cities.name FROM cities INNER JOIN states ON cities.state_id=states.id WHERE states.name LIKE %s ORDER BY cities.id"
#    cur.execute(query, state_n)
    rows = cur.fetchall()
    re = ""
    for row in rows:
        re += row[0] + ", "
    print(re[0:-2:])
        #if row[1] == state_n:
         #   print(row[1])
    cur.close()
    datab.close()


if __name__ == "__main__":
    cities_by_states()
