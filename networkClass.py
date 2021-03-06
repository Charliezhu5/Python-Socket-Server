import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.19" # server public(or local) address.
        self.port = 8080
        self.addr = (self.server, self.port)
        self.id = self.connect()
        self.user = "Charlie" # pls manually input an ID.
        print("{0} trying to initiate a connection with server on {1}:{2}".format(self.user, self.server, self.port))

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(str(e))
    
n = Network()
print(n.send(n.user))

while True:
        inp = input("You : ")

        if inp.lower() == "quit()":
            break

        print(n.send(inp))