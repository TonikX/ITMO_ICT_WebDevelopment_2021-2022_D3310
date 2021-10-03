# -*- coding:utf-8 -*-
"""
作者:酷酷酷
日期:2021年09月21日
"""
import socket
import math

server = socket.socket()
host = '127.0.0.1'
port = 6666
server.bind((host, port))
server.listen(3)

conn, addr = server.accept()
a_bin = conn.recv(1024)
b_bin = conn.recv(1024)
a = a_bin.decode('utf-8')
b = b_bin.decode('utf-8')
c = math.sqrt(int(a)**2 + int(b)**2)
conn.send(str(c).encode())
conn.close()