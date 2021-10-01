import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 10034))
c.send(b"Hello,server")
msg = c.recv(1024)
print(msg.decode("utf-8"))
c.close()
