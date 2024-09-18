import socket
import threading

clients = {}
routing_table = {}  # id <-> name

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.startswith('REGISTER'):
                _, name = message.split(' ')
                client_id = len(routing_table) + 1
                routing_table[client_id] = name
                clients[client_id] = client_socket
                client_socket.send(f"REGISTERED {client_id}".encode('utf-8'))
            elif message.startswith('MESSAGE'):
                _, target_name, msg = message.split(' ', 2)
                target_id = get_id_by_name(target_name)
                if target_id and target_id in clients:
                    clients[target_id].send(f"MESSAGE from {routing_table[target_id]}: {msg}".encode('utf-8'))
                    client_socket.send("DELIVERED".encode('utf-8'))
                else:
                    client_socket.send("USER_NOT_FOUND".encode('utf-8'))
        except:
            client_socket.close()
            break

def get_id_by_name(name):
    for client_id, client_name in routing_table.items():
        if client_name == name:
            return client_id
    return None

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(5)
    print("Server started and listening...")
    
    while True:
        client_socket, addr = server.accept()
        print(f"New connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
    