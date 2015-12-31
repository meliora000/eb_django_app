#Joseph Lee
#2015-12-23
#Migrate 'Incheon Coffee Shop' Text file data into Database

import sqlite3


#connect DB
conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

#open TXT data
f = open('incheon_coffee(7).txt','r')
d = f.readlines()

#integrate from TXT to DB
tname = "search_object"
num = 1
for i in d:
    Id,name,add,lat,lng = i.split(",")
    query = "INSERT INTO {0} VALUES ({5},'{1}','{2}',{3},{4})".format(tname,name,add,lat,lng,num)
    num+=1
    c.execute(query)

conn.commit()
print 'done'
