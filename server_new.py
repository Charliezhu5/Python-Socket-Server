print("Importing python libs......")
import socket
import threading
import sys

HEADER = 64 # the initial length of received message.
FORMAT = 'utf-8' # decoding using format.
PORT = 8080
SERVERADDR = socket.gethostbyname(socket.gethostname())
ADDR = (SERVERADDR, PORT)
DISCONNECT_MESSAGE = '!DISCONNECT'
print(f"[Server] The local address of this server is {ADDR}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[Server New Connection] Connected to {addr}.")

    while True:
        try:
            rcv_msg_length = conn.recv(HEADER).decode(FORMAT)
            rcv_msg_length = int(rcv_msg_length)
            rcv_msg = conn.recv(rcv_msg_length).decode(FORMAT)
            
            if rcv_msg == DISCONNECT_MESSAGE:
                conn.send(str(sys.getsizeof(f"Ok, bye......")).encode(FORMAT))
                conn.send(f"Ok, bye......".encode(FORMAT))
                break
            
            print(f"[Server Display] Received message '{rcv_msg}' from {addr}.")
            conn.send(str(sys.getsizeof(f"Message '{rcv_msg}' received!")).encode(FORMAT))
            conn.send(f"Message '{rcv_msg}' received!".encode(FORMAT))
        except:
            print("[Error] Something wrong!")
            break
    
    conn.close()
    print(f"[Server Lost Connection] Disconnected to {addr}.")

def start_server():
    server.listen()
    print("[Server] The server is now listening......")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Server Active Connections] {threading.activeCount() - 1}")

print("[Server] Initializing Server......")
start_server()
print("[Server] Server running, waiting for connection......")