import socket
import sys

SERVER = '192.168.1.19'
PORT = 8080
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MESSAGE = '!DISCONNECT'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(ADDR)
except:
    pass

while True:
        inp = input("You : ")

        if inp.lower() == "quit()":
            client_socket.send(str(sys.getsizeof(DISCONNECT_MESSAGE)).encode(FORMAT))
            client_socket.send(DISCONNECT_MESSAGE.encode(FORMAT))
            rcv_msg_len = client_socket.recv(HEADER).decode(FORMAT)
            rcv_msg_len = int(rcv_msg_len)
            rcv_msg = client_socket.recv(rcv_msg_len).decode(FORMAT)
            print(rcv_msg)
            break

        client_socket.send(str(sys.getsizeof(inp)).encode(FORMAT))
        client_socket.send(inp.encode(FORMAT))
        rcv_msg_len = client_socket.recv(HEADER).decode(FORMAT)
        rcv_msg_len = int(rcv_msg_len)
        rcv_msg = client_socket.recv(rcv_msg_len).decode(FORMAT)
        print(rcv_msg)