#!/usr/bin/python3
"""
Script that takes all args and displays all values in states
The script should be safe from MySQL injections
"""

import sys
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    cursor.close()
    db.close()
