#!/usr/bin/env python3
"""
Script qui liste tous les états (states) de la base de données hbtn_0e_0_usa.
Les résultats sont triés par ordre croissant selon l'id.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Récupère les arguments, se connecte à la BDD MySQL
    et affiche les lignes de la table 'states'.
    """
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

    cursor.close()
    db.close()
