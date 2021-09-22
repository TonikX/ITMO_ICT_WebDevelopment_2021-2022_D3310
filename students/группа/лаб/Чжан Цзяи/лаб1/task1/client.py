import socket

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 14900))
s.send(b"Hello, server")
data = s.recv(16384)
udata = data.decode('utf-8')
print(udata)
s.close()