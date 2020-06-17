print("Importing python libs......")
import socket
import threading
import sys
from protocol_server import get_msg, send_msg, get_userID, send_pickle, get_pickle
from sqlstuff import sql_inject
from classify import neural_classify
DISCONNECT_MESSAGE = '!DISCONNECT'

PORT = 8080
SERVERADDR = '192.168.1.19'
ADDR = (SERVERADDR, PORT)
print(f"[Server Info] The local address of this server is {ADDR}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    userID = str(get_userID(conn))
    print(f"[Server Info] Connected to {userID} @ {addr}.")

    while True:
        #try:
            rcv_msg = get_msg(conn,addr)
            sql_inject(rcv_msg, userID)
            
            # if case 1

            # if case 2
            # ...
            # if case n
            if rcv_msg == DISCONNECT_MESSAGE:
                break

            if rcv_msg.lower() == 'test()':
                obj = get_pickle(conn)
                print(f'[SERVER DEBUG] Received pickle obj: {obj}')
                obj1 = ('1','2','3')
                send_pickle(conn, addr, obj1)
                continue

            rply_msg = neural_classify(rcv_msg)
            send_msg(conn, addr, rply_msg)

        #except:
            # need more work on error handling.
            #print("[Server Error] Operation Error!")
            #break

    conn.close()
    print(f"[Server Info] Disconnected to {addr}.")

def start_server():
    server.listen()
    print("[Server Info] The server is now listening......")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Server Info] Active connection: {threading.activeCount() - 1}")

print("[Server Info] Initializing Server......")
start_server()