#Joseph Lee
#2015-12-23
#Migrate 'users' Text file data into Database

import sqlite3


#connect DB
conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

#open TXT data
f = open('users.txt','r')
d = f.readlines()

#integrate from TXT to DB
tname = "users_user"
for i in d:
    print i
    i = i.strip()
    a,b,c,d,e.f = i.split(",")
    query = "INSERT INTO users_user VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(a,b,c,d,e,f)
    c.execute(query)

conn.commit()
print 'done'
