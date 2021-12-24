import socket

newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newsocket.bind(("127.0.0.1", 9090))
newsocket.listen(5)

while True:
    client, addr = newsocket.accept()
    data = client.recv(1024).decode("utf-8")
    a, b = map(float,data.split(","))
    msg = "result = " + str(a*b)
    print(msg)
    client.sendall(msg.encode('utf-8'))
    client.close()