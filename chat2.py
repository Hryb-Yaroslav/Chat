import socket, threading

import Cezar

nickname = input("Введіть ім'я користувача:  ")
nickname = " >"+nickname
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
client.connect(('192.168.1.10', 53261))  
def receive():
        while True: 
            try:
                message = client.recv(1024).decode('utf-8')
                sd = (message).split("-")
                sn = Cezar.cesar(nickname, k)
                if sn not in sd and message != "NICKNAME":
                    s = input("""Вам проийшло повідомлення нажміть Enter щоб вибрати чи декодувати чи ні
                    /yes = декодувати, /no == не декодувати
                   (якщо дія не підтвердилась введіть щераз)""")
                    if s == "/yes":
                        print(Cezar.cesar(message, -k))
                    if s == "/no":
                        print(message)
                    if s != "/no" and s != "/yes":
                        print(message)
                        print("error")
                    #else:
                        #pass
                if message == 'NICKNAME':
                    client.send(nickname.encode('utf-8'))
            except:  
                print("Ошибка!")
                client.close()
                break
def write():
    while True:  
        a = input()
        if a == "" or a == "/yes" or a == "/no":
            pass
        elif a != "":
            print('{}- {}'.format(nickname, a))
            #mes = Cezar.cesar(a, k)
            message = Cezar.cesar('{}: {}'.format(nickname, a), k)
            client.send(message.encode('utf-8'))

k = 1
receive_thread = threading.Thread(target=receive) 
receive_thread.start()
write_thread = threading.Thread(target=write) 
write_thread.start()
