import socket

class Socket():
    def __init__(self, port, action, host='localhost'):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if action == "bind":
            self.socket.bind((host, port))
        elif action == "connect":
            self.socket.connect((host, port))

    def send(self, string):
        self.socket.send(string.encode())

    def recv(self):
        return self.socket.recv(1024).decode()

    def listen(self, num):
        self.socket.listen(num)

    def accept(self):
        return self.socket.accept()

    def close(self):
        self.socket.close()