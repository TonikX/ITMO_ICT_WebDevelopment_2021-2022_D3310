import socket                        # импорт socket
import threading                   # импорт threading

name = input("введите ваш имя")                                        # имя, которое клиент
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                  # создать TCP socket
c.connect(("127.0.0.1", 10101))                                        # клиент подклю. адрес

def receive():                                                         # определить функцию receive
    while True:                                                        # хотя правда
        try:                                                           # попробовать
            message = c.recv(23233).decode("utf-8")                    # отправить сообщение из клиента(мак.23233), кодировка по 'utf-8'
            if message == 'name':                                      # если сообщение определено как имя клиента
                c.send(name.encode("utf-8"))                           # отправить имя, кодировка по 'utf-8'
            else:                                                      # иначе
                print(message)                                         # печать сообщение
        except:
            print("error")                                             # печать ошибку
            c.close()                                                  # закрыто
            break                                                      # перерыв

def write():                                                           # определить функцию write
    while True:                                                        # хотя правда
        message = "{}:{}".format(name, input(""))                      # сообщение в форму '{имя клиента}:{сообщение}'
        c.send(message.encode("utf-8"))                                # отравить сообщение, кодировка по 'utf-8'

receive_thread = threading.Thread(target=receive)                      # многопоточность, target это заданная функция(здесь receive)
receive_thread.start()                                                 # начать
write_thread = threading.Thread(target = write)                        # многопоточность, target это заданная функция(здесь write)
write_thread.start()                                                   # начать
