import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 14900))
s.listen(3)
while True:
    c,addr = s.accept()
    
    data = c.recv(16384)
    while data:
        c.send(b"Hello client")
        udata = data.decode('utf-8')
        print(udata)
        break
    c.close()