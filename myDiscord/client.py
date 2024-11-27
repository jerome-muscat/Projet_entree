import socket

host, port = ('localhost', 3012)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host, port))
    nom = input('Enter your name: ')
    while True:
        data = input('Enter data: ')
        data = nom + ': ' + data
        data = data.encode('utf-8')
        sock.sendall(data)
    
except:
    print('Connection failed')

finally:
    sock.close()
