#!/usr/bin/python3
"""All states from database hbtn_0e_0_usa listd"""
import sys
import MySQLdb


if __name__ == "__main__":
    dtb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = dtb.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    dtb.close()
