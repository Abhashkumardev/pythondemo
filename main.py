import sqlite3
import csv
from datetime import datetime
import sys
import os

csv_file = str(sys.argv[1])
out = os.path.expanduser(csv_file)

f = open(out, 'r')  # open the csv data file
next(f, None)  # skip the header row
reader = csv.reader(f)

data = list(reader)

row_count = len(data)

sql = sqlite3.connect('person_db.db')
cur = sql.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS person
            (name text, age integer, created_at datetime)''')  # create the table if it doesn't already exist

count = 0
for row in data:
    time = datetime.now()
    row.append(time)
    count += 1
    cur.execute("INSERT INTO person VALUES (?, ?, ?)", row)

f.close()
sql.commit()
sql.close()
print(str(count) + " Records inserted, Total Records are " + str(row_count))