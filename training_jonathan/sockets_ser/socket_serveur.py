import socket

host_ip = '172.0.0.1'
host_port = 32000
max_data_sixe = 1024


s = socket.socket()
s.bind(('127.0.0.1', 32000))
s.listen()
print(f"attente de connection sur {host_ip}, port {host_port} ...  ")
connection_socket, client_address = s.accept()
print(f"Connection etablie avec {client_address} ")

while True:
    texte_envoye = input('Vous :  ')
    connection_socket.sendall(texte_envoye.encode())
    data_recu = connection_socket.recv(max_data_sixe)
    if not data_recu:
        break
    print(f"Message: {data_recu.decode()}")


s.close()