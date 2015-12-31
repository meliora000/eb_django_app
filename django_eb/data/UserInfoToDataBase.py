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
    name,userid,password,add,phone = i.split(",")
    query = "INSERT INTO {0} VALUES (null,'{1}','{2}','{3}','{4}','{5}')".format(tname,name,userid,password,add,phone)
    c.execute(query)

conn.commit()
print 'done'
