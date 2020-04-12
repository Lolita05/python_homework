#csv2tbl.py

import sqllite3
import io
import os.path
import glob


cnx = sqlite3.connect(user='user', host='localhost', password='password',
                                        database='dbname')
cursor=cnx.cursor(buffered= True)
path ='path/*/csv'
for files in glob.glob(path + "/*.csv"):
    add_csv_file="""LOAD DATA LOCAL INFILE '%s' INTO TABLE tabkename FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'  IGNORE 1 LINES;;;""" %(files)
    print ("add_csv_file: %s" % files)
    cursor.execute(add_csv_file)

cnx.commit()
cursor.close()
cnx.close()
