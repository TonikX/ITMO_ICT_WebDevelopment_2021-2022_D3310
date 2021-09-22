import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 14900))
s.listen()
clients = []
names = []
def talkbroad(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            message = client.recv(16384)
            talkbroad(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name =names[index]
            talkbroad('{} left'.format(name).encode('utf-8'))
            names.remove(name)
            break
def receive():
    while True:
        client, addr = s.accept()
        print("connected with {}".format(str(addr)))
        client.send('name'.encode('utf-8'))
        name = client.recv(16384).decode('utf-8')
        names.append(name)
        clients.append(client)
        print("name is {}".format(name))
        talkbroad("{} joined".format(name).encode('utf-8'))
        client.send('connected to server'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()