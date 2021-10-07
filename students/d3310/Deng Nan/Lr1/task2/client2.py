import socket

msg = input("Input numbers , use ',' to splits\n")
print(msg)
newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newsocket.connect(("127.0.0.1",9090))
newsocket.sendall(msg.encode('utf-8'))
data = newsocket.recv(1024).decode('utf-8')
print(data)