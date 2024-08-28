#db1.py

import sqlite3

# con = sqlite3.connect(':memory:')

con = sqlite3.connect('c:/work/sample.db')

cur = con.cursor()

cur.execute('create table PhoneBook (Name text, PhoneNum text);')

cur.execute("insert into PhoneBook values ('derick', '010-111');")

name = '전우치'
phoneNum = '010-222'
cur.execute('insert into PhoneBook values (?, ?);', (name, phoneNum))

datalist = (('이순신','010-123'),('박문수','010-567'))
cur.executemany('insert into PhoneBook values (?, ?);', datalist)

con.commit()

cur.execute('select * from PhoneBook;')

for row in cur:
    print(row)

# print('fetchon()')
# print(cur.fetchon())

# print('fetchmany(2)')
# print(cur.fetchmany(2))

# print('fetchall()')
# print(cur.fetchall())