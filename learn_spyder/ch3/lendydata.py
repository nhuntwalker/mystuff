# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:17:29 2015

@author: Nick
Lending library database API

Provides a CRUD interface to item and member entities and init and close
functions for database control.
"""
import sqlite3 as sql
db = None
cursor = None

##### CRUD functions for items #####
def insert_item(Name, Description, OwnerID, Price, Condition):
    query = """
    INSERT INTO item
    (Name, Description, OwnerID, Price, Condition, DateRegistered)
    VALUES (?,?,?,?,?, date('now'))"""

    cursor.execute(query, (Name, Description, OwnerID, Price, Condition))
    
def get_items():
    query = """
    SELECT ID, Name, Description, OwnerID, Price, Condition, DateRegistered
    FROM item"""
    return cursor.execute(query).fetchall()
    
def get_item_details(id):
    query = """
    SELECT Name, Description, OwnerID, Price, Condition, DateRegistered FROM
    item WHERE ID=?"""
    return cursor.execute(query,(id,)).fetchall()[0]
    
def get_item_name(id):
    return get_item_details(id)[0]

def update_item(id, Name=None, Description=None, OwnerID=None, Price=None, Condition=None):
    query = """
    UPDATE item SET Name=?, Description=?, OwnerID=?, Price=?, Condition=?
    WHERE ID=?"""
    data = get_item_details(id)
    if not Name:
        Name = data[0]
    if not Description:
        Description = data[1]
    if not OwnerID:
        OwnerID = data[2]
    if not Price:
        Price = data[3]
    if not Condition:
        Condition = data[4]
    
    cursor.execute(query, (Name, Description, OwnerID, Price, Condition, id))
    
def delete_item(id):
    query = """
    DELETE FROM item
    WHERE ID=?"""
    
    cursor.execute(query, (id,))

##### CRUD functions for members ######
def insert_member(name, email):
    query = """
    INSERT INTO member (name, email) VALUES (?,?)
    """
    
    cursor.execute(query, (name, email))
    
def get_members():
    query = """
    SELECT ID, Name, Email FROM member
    """
    return cursor.execute(query).fetchall()
    
def get_member_details(id):
    query = """
    SELECT Name, Email FROM member WHERE ID=?
    """
    return cursor.execute(query, (id,)).fetchall()[0]
    
def get_member_name(id):
    return get_member_details(id)[0]
    
def update_member(id, Name=None, Email=None):
    query = """
    UPDATE member SET Name=?, email=? WHERE id = ?
    """
    data = get_member_details(id)
    if not Name:
        Name = data[0]
    if not Email:
        Email = data[1]
    cursor.execute(query, (Name, Email, id))
    
def delete_member(id):
    query = """
    DELETE FROM member WHERE id=?
    """
    cursor.execute(query, (id,))
    
##### Database init and close ######
def initDB(filename=None):
    global db, cursor
    if not filename:
        filename = "lendy.db"
    try:
        db = sql.connect(filename)
        cursor = db.cursor()
    except:
        print("Error connecting to ", filename)
        cursor = None
        raise

def closeDB():
    try:
        cursor.close()
        db.commit()
        db.close()
    except:
        print("problem closing database...")
        raise

if __name__ == "__main__":
    initDB() # use default file
    print("Members:\n", get_members())
    print("Items:\n", get_items())
