# Secure-Login-System

This project consists of three Python scripts: samples.py, server.py, and client.py, which collectively facilitate a simple username and password authentication system using a SQLite database and client-server architecture.

samples.py:

Defines a SQLite database schema for storing user data, including usernames and hashed passwords.
Inserts sample user data into the database for testing purposes.
Utilizes hashlib to hash passwords before storing them in the database.
server.py:

Sets up a server using sockets to listen for incoming client connections.
Handles client connections by prompting for username and password.
Hashes the received password and compares it with the stored hashed password in the database.
Responds to the client indicating whether the login attempt was successful or not.
Uses threading to handle multiple client connections concurrently.
client.py:

Creates a client socket to connect to the server.
Sends a username and password to the server for authentication.
Receives a response from the server indicating the outcome of the login attempt and prints it.
Overall, this project demonstrates a basic client-server authentication system where clients can log in by providing a username and password, which are verified against data stored in a SQLite database on the server. However, it's important to note that for a real-world application, additional security measures such as encryption of data in transit and more robust authentication mechanisms would be necessary.
