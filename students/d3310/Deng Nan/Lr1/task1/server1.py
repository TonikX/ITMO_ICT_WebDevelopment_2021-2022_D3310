import socket

msg = "Hello,Client"

newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newsocket.bind(("127.0.0.1", 9090))
newsocket.listen(5)
while True:
    client, addr = newsocket.accept()
    data = client.recv(1024).decode('utf-8')
    client.sendall(msg.encode('utf-8'))
    print(data)
    client.close()