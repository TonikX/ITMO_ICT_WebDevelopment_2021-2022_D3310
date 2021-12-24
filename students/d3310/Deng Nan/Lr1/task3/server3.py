#server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host='localhost'
port=9999

server.bind((host,port))
server.listen(1)

paper = open('index.html')
copy = paper.read()
paper.close()

while 1:
    conn, addr = server.accept()
    print('Connected by', addr)
    conn.sendall(copy.encode('utf-8'))
    conn.close()
