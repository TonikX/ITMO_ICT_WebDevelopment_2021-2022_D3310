import socket


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('127.0.0.1', 555))
headers = [
    'GET / HTTP/1.1',
    'Host: 127.0.0.1',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(headers)
print(content)
conn.send(content.encode())
result = conn.recv(16384)
print(result.decode())