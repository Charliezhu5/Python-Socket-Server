print("Importing Libraries...")
import socket
from _thread import *
import sys
import pandas as pd
import pymysql
print("Importing Libraries...Done")

print("Setting pymysql parameters...")
connection = pymysql.connect(host="localhost", user="root", password="000000", db="chatbot_test")
cursor = connection.cursor()
data = {'Text':[], 'UserID':[]}
df = pd.DataFrame(data)
sql1 = "insert into messages(Text, UserID) values (%s, %s)"
print("Setting pymysql parameters...Done")

# connection setup:
PORT = 8080
server = "0.0.0.0"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, PORT))
except socket.error as e:
    print(str(e))

s.listen(5) # how many clients allowed.
print("Server started, waiting for a connection...")

# control of each connected client
def ThreadedClient(conn):

    conn.send(str.encode("Server: Connected to server. Please send me message..."))
    userID = conn.recv(2048).decode("utf-8")
    reply = ""

    while True:
        try:
            data = conn.recv(2048) # define how much of bits to receive information.
            receivedText = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else: # the part that handles received data.
                # below will simply inject client sent data to mysql server, and reply them result.
                print("Received data from user: {0}".format(userID))
                print("Injecting data to sql server....")
                injection = (receivedText, userID)
                cursor.execute(sql1, injection)
                print("Injecting data to sql server....Done")
                reply = "Server: Your input has been successfully logged."
                conn.sendall(str.encode(reply))

        except:
            print("Error at Threaded Client.")
            break
    
    print("Lost connection")
    conn.close()

# running loop.
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(ThreadedClient, (conn,)) # put ThreadedClient background as a new thread outside of loop. no need to wait for the funct.
