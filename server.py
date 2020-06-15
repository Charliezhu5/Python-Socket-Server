print("Importing python libs......")
import socket
import threading
import sys
from protocal_server_msg import get_msg_protocal, send_msg_protocal, get_userID
from sqlstuff import sql_inject
from classify import neural_classify

PORT = 8080
SERVERADDR = ''
ADDR = (SERVERADDR, PORT)
print(f"[Server Info] The local address of this server is {ADDR}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[Server Info] Connected to {addr}.")
    userID = str(get_userID(conn))

    while True:
        try: # need more work on error handling.
            rcv_msg = get_msg_protocal(conn,addr)
            sql_inject(rcv_msg, userID)
            rply_msg = neural_classify(rcv_msg)
            send_msg_protocal(conn, addr, rply_msg)
        except:
            print("[Server Error] Error!")
            break

    conn.close()
    print(f"[Server Info] Disconnected to {addr}.")

def start_server():
    server.listen()
    print("[Server Info] The server is now listening......")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Server Info] {threading.activeCount() - 1}")

print("[Server Info] Initializing Server......")
start_server()