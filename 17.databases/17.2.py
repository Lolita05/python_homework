#csv to db

import sqlite3 as sql
import csv

cnx = sql.connect('t.db')
cnx.execute('''CREATE TABLE IF NOT EXISTS t (
                                                        id INTEGER PRIMARY KEY,
                                                        diagnosis TEXT,
                                                        radius_mean FLOAT,
                                                        texture_mean FLOAT,
                                                        perimeter_mean FLOAT
                                                        )''')

with open('/Users/lolitiy/Desktop/data.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile, delimiter=';')
    to_db = [(i['diagnosis'], i['radius_mean'], i['texture_mean'], i['perimeter_mean']) for i in myCSVReader]


cnx.executemany("INSERT INTO t (diagnosis, radius_mean, texture_mean, perimeter_mean) VALUES (?, ?, ?, ?);", to_db)
cnx.commit()

alter = '''ALTER TABLE t ADD COLUMN sex'''
cnx.execute(alter)
cnx.commit()

cnx.execute('''CREATE TABLE IF NOT EXISTS t2 (
                                                        id INTEGER PRIMARY KEY,
                                                        diagnosis TEXT,
                                                        sex TEXT
                                                        )''')
cnx.commit()

#Тут пишет что таблицы t2 нет - почемууу
query_t2 = [(1, 'M', 'm'),
            (2, 'M', 'w'),
            (3, 'M', 'w'),
            (4, 'M', 'm'),
            (5, 'M', 'm'),
            (6, 'M', 'w'),
            (7, 'M', 'w'),
            (8, 'M', 'm'),
            (9, 'M', 'm'),
            (10, 'M', 'w'),
            (11, 'M', 'w'),
            (12, 'M', 'm'),
            (13, 'M', 'm'),
            (14, 'M', 'w'),
            (15, 'M', 'w'),
            (16, 'M', 'm'),
            (17, 'M', 'm'),
            (18, 'M', 'w')]

cnx.executemany('''INSERT INTO t2 VALUES (?, ?, ?)''', query_t2)

cnx.commit()

query = ''' INSERT INTO t (sex) SELECT (sex) FROM t2'''
cnx.execute(query)
cnx.commit()
