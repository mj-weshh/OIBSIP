import socket
import threading


def handle_client(client_socket, address):
    """
    Handles communication with a connected client.

    Args:
    - client_socket: The socket object for the connected client.
    - address: The address (IP, port) of the connected client.
    """

    while True:
        # Receive message from the client
        message = client_socket.recv(1024).decode('UTF-8')

        # Check if the client wants to exit        
        if message == exit:
            print(f"\nConnection with {address} ended.")
            break
        # Display received message from the client
        print(f"\nMessage from {address}: {message}")
        # Get user input for response
        response = input(f"Enter response to {address}:")
        # Send the response back to the client
        client_socket.send(response.encode('UTF-8'))


def initialize_server():
    """
    Initializes the server socket and listens for incoming connections.
    Creates a new thread to handle each connected client.
    """
    # Create a server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the server to a specific address and port
    server.bind(('0.0.0.0', 12345))
    # Listen for incoming connections, allowing up to 2 clients in the queue
    server.listen(2)
    print("\nServer is listening ...")
    
    while True:
        # Accept incoming connection
        client_socket, address = server.accept()
        print(f"\n{address} connection accepted")
        # Create a new thread to handle the connected client
        client_handler = threading.Thread(target = handle_client, args=(client_socket, address))
        client_handler.start()


if __name__ == "__main__":
    initialize_server()
