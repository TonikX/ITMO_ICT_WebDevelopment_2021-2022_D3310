#client
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host='localhost'
port=9999

server.connect((host,port))
msg = server.recv(1024).decode('utf-8')
print(msg)

server.close()
