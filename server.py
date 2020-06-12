import socket
from _thread import *
import sys

PORT = 8080
server = "0.0.0.0"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, PORT))
except socket.error as e:
    print(str(e))

s.listen(5) # how many clients allowed.
print("Server started, waiting for a connection...")

def ThreadedClient(conn):

    conn.send(str.encode("Connected to server."))
    reply = ""

    while True:
        try:
            data = conn.recv(2048) # define how much of bits to receive information.
            reply = data.decode("utf-8") # echoing.

            if not data:
                print("Disconnected")
                break
            else: # the part that handles received data.
                print("Received: ", reply)
                print("Sending: ", reply)
                conn.sendall(str.encode(reply))

        except:
            print("Error at Threaded Client.")
            break
    
    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(ThreadedClient, (conn,)) # put ThreadedClient background as a new thread outside of loop. no need to wait for the funct.
