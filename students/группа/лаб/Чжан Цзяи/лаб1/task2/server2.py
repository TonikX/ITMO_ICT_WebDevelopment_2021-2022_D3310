import socket
import struct
from math import *


def htonfl(f):
    s = struct.pack('d',f)
    return struct.unpack('!Q',s)[0]


def max_l(a, b):
    return sqrt(pow(a, 2) + pow(b, 2))


def min_l(m, n):
    if m == n:
        return 'нельзя равно'
    else:
        return sqrt(abs(pow(m, 2) - pow(n, 2)))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 14900))
s.listen(5)
while True:
    c, addr = s.accept()
    data = c.recv(16384)
    udata = list(data)
    if 1 in udata:
        result = max_l(udata[1], udata[2])
        a = struct.pack('!f', result)
        c.send(a)
    elif 2 in udata:
        result1 = min_l(udata[1], udata[2])
        b = struct.pack('!f', result)
        c.send(b)
    else:
        c.send(b"write 'Y' or 'N'")
    c.close()