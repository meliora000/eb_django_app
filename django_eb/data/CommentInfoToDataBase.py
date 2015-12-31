#Joseph Lee
#2015-12-31
#Create Random Comment
from __future__ import unicode_literals
import sqlite3
import random
from random import sample

#connect DB
conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

#User
user = ['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh']

#Comment
infile = open("comment.txt","r")
comment = [i.strip() for i in infile.readlines()]

#Table name
tname = 'comment_comment'

#Insert Into comment_comment 4 randomUser 4 random Comment to each 1 ~ 1521 CoffeeShop

for coffeeid in range(1,1522):
    for userN in sample(xrange(8),4):
        userID = user[userN]
        commentIs = comment[random.randint(0,7)]
        query = "INSERT INTO {0} VALUES (null,'{1}','{2}','{3}',{4},'{5}','{6}');".format(tname,bool(random.getrandbits(1)),bool(random.getrandbits(1)),commentIs.decode('utf-8'),coffeeid,userID,bool(random.getrandbits(1)))
        c.execute(query)

    if(coffeeid % 100 == 0):
        print coffeeid

conn.commit()
print'done'