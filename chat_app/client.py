import socket
import threading


def recieve_message(client_socket):
    """
    Receives and displays messages from the server.

    Args:
    - client_socket: The socket object for the client.
    """

    while True:
        # Receive message from the server
        message = client_socket.recv(1024).decode('UTF-8')
        # Display the received message
        print(f"\nMessage from server: {message}")
        # Break the loop if the message is received
        break
 
        
def initialize_client():
    """
    Initializes the client socket, connects to the server, and starts a thread
    to receive messages from the server. Allows the user to send messages to the server.
    """
    # Create a client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server at the specified address and port
    client.connect(('127.0.0.1', 12345))
    # Start a thread to receive messages from the server
    recieve_thread = threading.Thread(target= recieve_message, args=(client,))
    recieve_thread.start()
    
    while True:
        # Get user input for a message
        user_input = input("\nEnter message ('exit' to end chat): ")
        # Send the user input to the server
        client.send(user_input.encode('UTF-8'))
        # Break the loop if the user wants to exit the chat
        if user_input.lower() == 'exit':
            break

        
if __name__ == "__main__":
    initialize_client()
