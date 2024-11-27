import socket
import threading

def receive_data(sock):
    while True:
        response = sock.recv(1024).decode('utf-8')
        print(response)

host, port = ('10.10.3.195', 3012)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host, port))
    nom = input('Enter your name: ')

    # Lancement du thread pour la réception des données du serveur
    thread_receive = threading.Thread(target=receive_data, args=(sock,))
    thread_receive.start()

    while True:
        data = input('Enter data: ')
        data = nom + ': ' + data
        data = data.encode('utf-8')
        sock.sendall(data)
    
except:
    print('Connection failed')

finally:
    sock.close()
