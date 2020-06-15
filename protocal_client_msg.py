import sys

FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MESSAGE = '!DISCONNECT'

def get_msg_protocal(client_socket, inp):
    if inp.lower() == "quit()":
        client_socket.send(str(sys.getsizeof(DISCONNECT_MESSAGE)).encode(FORMAT))
        client_socket.send(DISCONNECT_MESSAGE.encode(FORMAT))
        rcv_msg_len = client_socket.recv(HEADER).decode(FORMAT)
        rcv_msg_len = int(rcv_msg_len)
        rcv_msg = client_socket.recv(rcv_msg_len).decode(FORMAT)
        print(rcv_msg)
        raise Exception

    client_socket.send(str(sys.getsizeof(inp)).encode(FORMAT))
    client_socket.send(inp.encode(FORMAT))
    
    rcv_msg_len = client_socket.recv(HEADER).decode(FORMAT)
    rcv_msg_len = int(rcv_msg_len)
    rcv_msg = client_socket.recv(rcv_msg_len).decode(FORMAT)
    print(rcv_msg)

def send_userID(client_socket, ID):
    client_socket.send(ID.encode(FORMAT))