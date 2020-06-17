import socket
import sys
from protocol_client import get_msg, send_msg, send_userID, end_connection, send_pickle, get_pickle

SERVER = '192.168.1.19'
PORT = 8080
ADDR = (SERVER, PORT)
ID = 'Name' # Your name will be your ID, no more than 64 characters.


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(ADDR)
    send_userID(client_socket, ID)
except:
    pass

while True:

    inp = input(f"{ID} : ")

    #try:

    send_msg(client_socket,inp)

    if inp.lower() == "quit()":
        end_connection(client_socket)
        print("You quit.")
        break

    if not inp:
        print("[Warning] Input cannot be empty!!! Please try again.")
        continue

    if inp.lower() == 'test()':
        test = ('1', '2', '3', '4', '5')
        send_pickle(client_socket, test)
        data = get_pickle(client_socket)
        print(data)
        continue

    print(get_msg(client_socket))

    #except:
        #break