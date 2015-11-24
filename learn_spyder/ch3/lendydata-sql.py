# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:21:38 2015

@author: Nick
"""

import sqlite3
db = sqlite3.connect("./lendy.db")
cursor = db.cursor()

#sql1 = "PRAGMA Foreign_Keys = True;"
sql2 = "DROP TABLE loan;"
sql3 = "DROP TABLE item;"
sql4 = "DROP TABLE member;"
sql5 = "CREATE TABLE member (ID INTEGER PRIMARY KEY,Name TEXT NOT NULL,Email TEXT);"
sql6 = "CREATE TABLE item (ID INTEGER PRIMARY KEY,Name TEXT NOT NULL,Description TEXT NOT NULL,OwnerID INTEGER NOT NULL REFERENCES member(ID),Price NUMERIC,Condition TEXT,DateRegistered TEXT);"
sql7 = "CREATE TABLE loan (ID INTEGER PRIMARY KEY,ItemID INTEGER NOT NULL REFERENCES item(ID),BorrowerID INTEGER NOT NULL REFERENCES member(ID),DateBorrowed TEXT,DateReturned TEXT);"

#cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
cursor.execute(sql6)
cursor.execute(sql7)


members = [
["Fred", "fred@lendylib.org"],
["Mike", "mike@gmail.com"],
["Joe", "joe@joesmail.com"],
["Rob", "rjb@somcorp.com"],
["Anne", "annie@bigbiz.com"]]
member_sql = "INSERT INTO member (Name, Email) VALUES (?, ?);"

items = [
['Lawnmower', 'Tool', 0, 150, 'Excellent', '2012-01-05'],
['Lawnmower', 'Tool', 0, 370, 'Fair', '2012-04-01'],
['Bike', 'Vehicle', 0, 200, 'Good', '2013-03-22'],
['Drill', 'Tool', 0, 100, 'Good', '2013-10-28'],
['Scarifier', 'Tool', 0, 200, 'Average', '2013-09-14'],
['Sprinkler', 'Tool', 0, 80, 'Good', '2014-01-06']]
item_sql = """
INSERT INTO item 
(Name, Description, OwnerID, Price, Condition, DateRegistered)
VALUES (?, ?, ?, ?, ?, date(?));
"""

set_owner_sql = """
UPDATE item set OwnerID = 
(SELECT ID FROM member WHERE name = ?)
WHERE item.ID = ?;
"""

loans = [
['1','3','2012-4-1','2012-4-26'],
['2','5','2012-9-5','2013-1-5'],
['3','4','2013-7-3','2013-7-22'],
['4','1','2013-11-19','2013-11-29'],
['5','2','2013-12-5',None]
]
loan_sql = """
INSERT INTO loan
(ItemID, BorrowerID, DateBorrowed, DateReturned)
VALUES (?, ?, date(?), date(?));
"""

cursor.executemany(member_sql, members)
cursor.executemany(item_sql, items)
cursor.executemany(loan_sql, loans)

owners = ('Fred', 'Mike', 'Joe', 'Rob', 'Anne', 'Fred')
for item in cursor.execute("SELECT ID FROM item").fetchall():
    itemID = item[0]
    cursor.execute(set_owner_sql, (owners[itemID-1], itemID))
    
cursor.close()
db.commit()
db.close()