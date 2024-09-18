import socket

def send_message(sock, message):
    sock.send(message.encode('utf-8'))
    response = sock.recv(1024).decode('utf-8')
    print("Server response:", response)

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))
    
    # Регистрация
    name = input("Enter your name: ")
    send_message(client, f"REGISTER {name}")
    
    # Отправка сообщений
    while True:
        recipient = input("Send to (name): ")
        message = input("Message: ")
        send_message(client, f"MESSAGE {recipient} {message}")