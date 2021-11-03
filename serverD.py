import socket, threading  

import Cezar

host = '192.168.1.10' 
port = 53261  

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((host, port))  
server.listen()

clients = []
nicknames = []


def broadcast(message):  
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:  
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            #broadcast('{} вийшов!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break


def receive(): 
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
