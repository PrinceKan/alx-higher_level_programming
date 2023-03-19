#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa
    it should take 3 arguments: mysql username, mysql password
    and database name
"""
import sys
import MySQLdb


def list_states():
    """connects to the given mysql database and lists all 'states' from this"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db_connect = MySQLdb.connect("localhost",
                                 mysql_username,
                                 mysql_password,
                                 database_name,
                                 3306)
    cursor = db_connect.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
             LEFT JOIN states ON cities.state_id = states.id\
             ORDER BY cities.id ASC;")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db_connect.close()


if __name__ == '__main__':
    list_states()
