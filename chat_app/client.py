import socket
import threading


def recieve_message(client_socket):
    while True:
        message = client_socket.recv(1024).decode('UTF-8')
        print(f"\nMessage from server: {message}")
        break
 
        
def initialize_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))
    recieve_thread = threading.Thread(target= recieve_message, args=(client,))
    recieve_thread.start()
    
    while True:
        user_input = input("\nEnter message ('exit' to end chat): ")
        client.send(user_input.encode('UTF-8'))
        if user_input.lower() == 'exit':
            break

        
if __name__ == "__main__":
    initialize_client()