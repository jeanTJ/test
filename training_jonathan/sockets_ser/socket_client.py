import socket
import time


host_ip = '127.0.0.1'
host_port = 32000
max_data_sixe = 1024



print(f"connection au serveur {host_ip}, port {host_port}")
while True:
    try:
        s = socket.socket()
        s.connect((host_ip, host_port))
        print('connecte au serveur')
        break
    except ConnectionRefusedError:
        print("ERREUR : impossible de se connecte au serveur . Reconnection..." )
        time.sleep(3)

while True:
    data_recu = s.recv(max_data_sixe)
    if not data_recu == '':
        break
    print(f"Message: {data_recu.decode()}")
    envoie = input(f"Vous: ")
    s.sendall(envoie.encode())




s.close()

