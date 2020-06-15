# The message protocal follows this pattern. Server always wait on first message containing message length, then second message is
# the actual message. After receiving the actual message, server send its reply length followed by reply.
import sys

HEADER = 64 # the initial length of received message.
FORMAT = 'utf-8' # decoding using format.
DISCONNECT_MESSAGE = '!DISCONNECT'

def get_msg_protocal(conn, addr):

    rcv_msg_length = conn.recv(HEADER).decode(FORMAT)
    rcv_msg_length = int(rcv_msg_length)
    rcv_msg = conn.recv(rcv_msg_length).decode(FORMAT)
    
    if rcv_msg == DISCONNECT_MESSAGE:
        conn.send(str(sys.getsizeof(f"Ok, bye......")).encode(FORMAT))
        conn.send(f"Ok, bye......".encode(FORMAT))
        raise Exception

    print(f"[Server Display] Received message '{rcv_msg}' from {addr}.")
    return rcv_msg

def send_msg_protocal(conn, addr, rply_msg):
    conn.send(str(sys.getsizeof(rply_msg)).encode(FORMAT))
    conn.send(rply_msg.encode(FORMAT))
    print(f"[Server Display] Sent message '{rply_msg}' to {addr}.")

def get_userID(conn):
    return conn.recv(HEADER).decode(FORMAT)