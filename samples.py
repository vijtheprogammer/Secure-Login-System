import sqlite3
import hashlib #hash the passwords 


connect = sqlite3.connect("userdata.db")
cur = connect.cursor()

#create database
cur.execute(""" 
    CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

username1, password1 = "mike213", hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "john", hashlib.sha256("ohnowhy".encode()).hexdigest()
username3, password3 = "xxxttt", hashlib.sha256("jsoa3@4nfao".encode()).hexdigest()
username4, password4 = "iatefood", hashlib.sha256("trainsarecool".encode()).hexdigest()

#insert data
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

connect.commit()

#cur.execute("SELECT * FROM userdata")

