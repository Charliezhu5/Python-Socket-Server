# The message protocol follows this pattern. Server always wait on first message containing message length, then second message is
# the actual message. After receiving the actual message, server send its reply length followed by reply.
import sys
import pickle

HEADER = 10 # the initial length of received message.
FORMAT = 'utf-8' # decoding using format.

def get_msg(conn, addr):
    rcv_msg_length = conn.recv(HEADER).decode(FORMAT)
    rcv_msg_length = int(rcv_msg_length)
    rcv_msg = conn.recv(rcv_msg_length).decode(FORMAT)
    print(f"[Server Display] Received message '{rcv_msg}' from {addr}.")
    return rcv_msg

def send_msg(conn, addr, rply_msg):
    conn.send(str(sys.getsizeof(rply_msg)).encode(FORMAT))
    conn.send(rply_msg.encode(FORMAT))
    print(f"[Server Display] Sent message '{rply_msg}' to {addr}.")

def get_userID(conn):
    return conn.recv(HEADER).decode(FORMAT)

def get_pickle(conn):
    size = int(conn.recv(HEADER).decode(FORMAT))
    data = conn.recv(size)
    return pickle.loads(data)
    
def send_pickle(conn, addr, obj):
    data = pickle.dumps(obj)
    size = f"{sys.getsizeof(data):<{HEADER}}".encode(FORMAT)
    conn.send(size)
    conn.send(data)
    print(f"[Server Display] Sent an obj to {addr}.")