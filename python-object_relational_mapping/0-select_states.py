#!/usr/bin/env python3
import sys
import MySQLdb


# Les arguments du script sont accessibles avec sys.argv
# sys.argv[1] : username MySQL
# sys.argv[2] : password MySQL
# sys.argv[3] : database name

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database
)

cursor = db.cursor()

cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

rows = cursor.fetchall()

for row in rows:
    print(row)
