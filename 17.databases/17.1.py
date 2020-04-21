#Прочитайте о следующих командах и попробуйте их - UPDATE, DELETE, CASCADE

import sqlite3 as sql

#create connection
connection = sql.connect('first.db')
#create table
connection.execute('''CREATE TABLE IF NOT EXISTS first (
                                                        id INTEGER PRIMARY KEY,
                                                        first_name TEXT,
                                                        last_name TEXT,
                                                        age TEXT,
                                                        sex TEXT
                                                        )''')

people = [('1', 'Vasya', 'Noname', '23', 'male'),
          ('2', 'Yoda', 'nodata', '900', 'male'),
          ('3', 'Xanathar', 'the Eye', 'nodata', 'male')]

query = ''' INSERT INTO first VALUES (?, ?, ?, ?, ?)'''

#add data into table
connection.executemany(query, people)
#commit changes
connection.commit()
#close connection
connection.close()

#UPDATE
connection = sql.connect('first.db')

sql = """
UPDATE first 
SET last_name = 'Pupkin' 
WHERE last_name = 'Noname'
"""
connection.execute(sql)
connection.commit()

#DELETE
sql1 = "DELETE FROM first WHERE first_name = 'Vasya'"

connection.execute(sql1)
connection.commit()

#CASCADE

connection.execute('''CREATE TABLE IF NOT EXISTS second (
                                                        id INTEGER PRIMARY KEY,
                                                        name TEXT REFERENCES first(first_name) ON UPDATE CASCADE
                                                        )''')
connection.commit()

connection.close()