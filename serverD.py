import socket, threading  # Импорт библиотек

import Cezar

host = '192.168.1.10'  # Локальный хост компьютера
port = 53261  # Выбор незарезервированного порта

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Инициализация сокета
server.bind((host, port))  # Назначение хоста и порта к сокету
server.listen()

clients = []
nicknames = []


def broadcast(message):  # Функция связи
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:  # Получение сообщений от клиента
            message = client.recv(1024)
            broadcast(message)
        except:  # Удаление клиентов
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            #broadcast('{} вийшов!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break


def receive():  # Подключение нескольких клиентов
    while True:
        client, address = server.accept()
        print("Соединён с {}".format(str(address)))
        client.send('NICKNAME'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print("Имя пользователя {}".format(nickname))
        #broadcast("{} 111".format(nickname).encode('utf-8'))
        #client.send('22!22'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()