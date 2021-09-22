import socket
import struct

q = input("Хотите ли вы вычислить гипотенузу?Ответ по 'Y' или 'N'")
j = int(input("Первая длина стороны"))
k = int(input("Вторая длина стороны"))


if q == 'Y':
    lst = [1, j, k]
elif q == 'N':
    lst = [2, j, k]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 14900))
s.send(bytearray(lst))
data = s.recv(16384)
udata = struct.unpack('!f', data)
print(udata)
s.close()