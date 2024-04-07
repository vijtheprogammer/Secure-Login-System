import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9997))

server.listen()

def handle_conn(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()


    connect = sqlite3.connect("userdata.db")
    cur = connect.cursor()

    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))

    if cur.fetchall():
        c.send("Login successful!".encode())
    else:
        c.send("Login failed!".encode())

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_conn, args=(client,)).start()


