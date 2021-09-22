import random
import socket
import time


server = socket.socket()
host = '127.0.0.1'
port = 555
server.bind((host, port))
print('Starting server on', host, port)
print('The Web server URL for the would be http://%s:%d' % (host, port))
server.listen(5)
print('Entering infinite loop; hit CTRL-C to exit')
while True:
    client, (client_host, client_port) = server.accept()
    print('Got connection from', client_host, client_port)
    client.recv(1000)
    response_type = 'HTTP/1.0 200 ok\n'
    headers = 'Content-Type: text/html\n\n'
    body = """
        <html>
        <body>
        <h1>Hello World</h1>!
        </body>
        </html>
    """
    response = response_type + headers + body
    client.send(response.encode('utf-8'))
    client.close()