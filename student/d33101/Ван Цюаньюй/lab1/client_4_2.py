import socket
import threading

name = input("введите ваш имя")
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 10101))

def receive():
    while True:
        try:
            message = c.recv(23233).decode("utf-8")
            if message == 'name':
                c.send(name.encode("utf-8"))
            else:
                print(message)
        except:
            print("error")
            c.close()
            break

def write():
    while True:
        message = "{}:{}".format(name, input(""))
        c.send(message.encode("utf-8"))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target = write)
write_thread.start()
