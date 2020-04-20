#csv to db

import sqlite3 as sql
import csv

cnx = sql.connect('t.db')
cnx.execute('''CREATE TABLE IF NOT EXISTS t (
                                                        id INTEGER PRIMARY KEY,
                                                        diagnosis FLOAT,
                                                        radius_mean FLOAT,
                                                        texture_mean FLOAT,
                                                        perimeter_mean FLOAT
                                                        )''')

with open('/Users/lolitiy/Desktop/data.csv') as csvfile:
    myCSVReader=csv.DictReader(csvfile, delimiter=';')
    to_db = [(i['diagnosis'], i['radius_mean'], i['texture_mean'], i['perimeter_mean']) for i in myCSVReader]

cnx.executemany("INSERT INTO t (diagnosis, radius_mean, texture_mean, perimeter_mean) VALUES (?, ?, ?, ?);", to_db)
cnx.commit()


