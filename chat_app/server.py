import socket
import threading


def handle_client(client_socket, address):
    while True:
        message = client_socket.recv(1024).decode('UTF-8')
        if message == exit:
            print(f"\nConnection with {address} ended.")
            break
        print(f"\nMessage from {address}: {message}")
        response = input(f"Enter response to {address}:")
        client_socket.send(response.encode('UTF-8'))


def initialize_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(2)
    print("\nServer is listening ...")
    
    while True:
        client_socket, address = server.accept()
        print(f"\n{address} connection accepted")
        client_handler = threading.Thread(target = handle_client, args=(client_socket, address))
        client_handler.start()


if __name__ == "__main__":
    initialize_server()