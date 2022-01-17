import socket                        # импорт socket
import threading                    # импорт threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # создать TCP socket
s.bind(("127.0.0.1", 10101))                                      # адрес привязки(host, port)
s.listen()                                                        # начать прослушивание TCP
clients = []                                                      # создать лист клиента
names = []                                                        # создать лист имени

def talkbroad(message):                                           # определить функцию talkbroad, чтобы ввод сообщение
    for client in clients:                                        # для client в clients
        client.send(message)                                      # клиент отправит сообщение

def handle(client):                                               # определить функцию handle, для клиента
    while True:                                                   # хотя правда
        try:                                                      # попробовать
            message = client.recv(23233)                          # принять сообщение из клиента(мак.23233)
            talkbroad(message)                                    # к предыдущей функции
        except:
            index = clients.index(client)                         # индекс клиента
            clients.remove(client)                                # удалить клиента из листа клиентов
            client.close()                                        # закрыто
            name = names[index]                                   # имя клиентов из индекса
            talkbroad('{} list'.format(name).encode('utf-8'))     # имя, которое введил, кодировка по 'utf-8'
            names.remove(name)                                    # удалить имя
            break                                                 # перерыв

def receive():                                                    # определить функцию receive
    while True:                                                   # хотя правда
        client, addr = s.accept()                                 # пассивное принятие клиентских ссылок TCP
        print("connected with {}".format(str(addr)))              # печать связь с адреса
        client.send("name".encode("utf-8"))                       # клиент отправит имя, кодировка по 'utf-8'
        name = client.recv(23233).decode("utf-8")                 # имя из клента(мак.23233), кодировка по 'utf-8'
        names.append(name)                                        # добавить имя
        clients.append(client)                                    # добавить клиента
        print("name is {}".format(name))                          # печать имя это {}
        talkbroad("{} joined".format(name).encode("utf-8"))       # в talkbroad, кто вступить, кодировка по 'utf-8'
        client.send("connected to server".encode("utf-8"))        # отправка в клиент 'connected to server', кодировка по 'utf-8'
        thread = threading.Thread(target=handle, args=(client,))  # многопоточность, target это заданная функция(здесь handle), args это переданные параметры перечня
        thread.start()                                            # начать
receive()