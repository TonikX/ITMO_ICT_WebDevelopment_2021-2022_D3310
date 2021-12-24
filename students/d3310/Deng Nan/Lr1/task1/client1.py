import socket

msg = "Hello, Server"
newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newsocket.connect(("127.0.0.1",9090))
newsocket.sendall(msg.encode('utf-8'))
data = newsocket.recv(1024).decode('utf-8')
print(data)
newsocket.close()