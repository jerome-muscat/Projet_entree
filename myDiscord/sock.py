import socket
import threading

class Sock(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        while True:
            data = self.conn.recv(1024)
            data = data.decode('utf-8')
            print(f"{self.addr}: {data}")

            # Parcourir toutes les connexions actives
            for client_conn, client_addr in connections:
                # Vérifier que la connexion n'est pas celle du client actuel
                if client_conn != self.conn:
                    # Envoyer les données au client
                    client_conn.sendall(data.encode('utf-8'))

host, port = ('10.10.3.195', 3012)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

# Liste des connexions actives
connections = []

while True:
    sock.listen()
    conn, addr = sock.accept()

    # Ajouter la connexion à la liste des connexions actives
    connections.append((conn, addr))

    # Créer un thread pour gérer la connexion
    my_thread = Sock(conn, addr)
    my_thread.start()