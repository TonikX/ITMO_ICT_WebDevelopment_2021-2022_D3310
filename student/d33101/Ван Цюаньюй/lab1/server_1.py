import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 10034))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    msg = clientsocket.recv(1024)
    print(msg.decode("utf-8"))
    clientsocket.send(bytes("Hello,client", "utf-8"))
    clientsocket.close()
