import socket
import sys
from protocal_client_msg import get_msg_protocal, send_userID

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

        try:
            get_msg_protocal(client_socket, inp)
        except:
            break