#Прочитайте о следующих командах и попробуйте их - UPDATE, DELETE, CASCADE

import sqlite3 as sql

#create connection
connection = sql.connect('first.db')
cursor = connection.cursor()

#create table
cursor.execute = (''' CREATE TABLE IF NOT EXISTS first (
    ID INTEGER,
    first_name TEXT,
    last_name TEXT,
    age TEXT,
    sex TEXT ON UPDATE CASCADE
    )''')

people = [('1', 'Vasya', 'Noname', '23', 'male'),
          ('2', 'Yoda', 'nodata', '900', 'male'),
          ('3', 'Xanathar', 'the Eye', 'nodata', 'male')]

#add data into table
cursor.executemany = (' INSERT INTO first VALUES (?, ?, ?, ?, ?)', people)

#commit changes
connection.commit()

#close connection
connection.close()

#UPDATE
connection = sql.connect('first.db')
cursor = connection.cursor()

sql = """
UPDATE first 
SET last_name = 'Pupkin' 
WHERE last_name = 'Noname'
"""
cursor.execute(sql)
connection.commit()

#DELETE
sql = "DELETE FROM first WHERE first_name = 'Vasya'"

cursor.execute(sql)
connection.commit()

