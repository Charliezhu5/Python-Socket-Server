import sys
import pickle

FORMAT = 'utf-8'
HEADER = 10
DISCONNECT_MESSAGE = '!DISCONNECT'

def get_msg(client_socket):  
    rcv_msg_len = client_socket.recv(HEADER).decode(FORMAT)
    rcv_msg_len = int(rcv_msg_len)
    rcv_msg = client_socket.recv(rcv_msg_len).decode(FORMAT)
    return rcv_msg

def send_msg(client_socket, inp):
    client_socket.send(str(sys.getsizeof(inp)).encode(FORMAT))
    client_socket.send(inp.encode(FORMAT))

def send_userID(client_socket, ID):
    client_socket.send(ID.encode(FORMAT))

def end_connection(client_socket):
    client_socket.send(str(sys.getsizeof(DISCONNECT_MESSAGE)).encode(FORMAT))
    client_socket.send(DISCONNECT_MESSAGE.encode(FORMAT))

def send_pickle(client_socket, obj):
    data = pickle.dumps(obj)
    size = f"{sys.getsizeof(data):<{HEADER}}".encode(FORMAT)
    client_socket.send(size)
    client_socket.send(data)

def get_pickle(client_socket):  
    size = int(client_socket.recv(HEADER).decode(FORMAT))
    data = client_socket.recv(size)
    return pickle.loads(data)