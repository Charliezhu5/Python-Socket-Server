# Python-Socket-Server
Chatbot socket server and client --version 0.0

A python socket server that listens to clients on internet. It handles different types of requests.
The server is also backed up with mySQL using pymysql as API to communicate with the database.

The server consists of multiple python files, each serves as a module to provide functions:

server.py: the implementation of the server. To keep its code clean, it should only uses other module to realize some functions.
protocol_server.py: provides some protocols for server.py to realize different communication. Each protocol should also pair with a client protocol.
protocol_client.py: client side protocol. Each protocol should pair with a server side protocol.

neural.py: the core of machine learning unit.
classify.py: using neural.py to classify the intent of a sentence.

sqlstuff.py: provide pymysql APIs to realize database function.


what it does:
Each connection is handled in a thread.
In each thread, the server first waiting for client sending their ID. then this ID will be used for database insertion.
then client will send msg to server, and base on what the msg is there will be different subroutines.
pickle transfer protocol.


What I plan to do:
setup training command.
setup select model command.
