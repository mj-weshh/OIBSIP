# Simple Command-Line Chat Application

This is a basic command-line chat application implemented in Python, consisting of a server (`server.py`) and a client (`client.py`). The application allows two users to exchange messages in real-time through the command line.

## Usage

### Server (`server.py`)

1. Run the server script using the following command:
   ```bash
   python server.py
   ```
2. The server will listen for incoming connections on IP `0.0.0.0` and port `12345`.

### Client (`client.py`)

1. Run the client script using the following command:
   ```bash
   python client.py
   ```
2. The client will connect to the server at `127.0.0.1` on port `12345`.
3. Enter messages to send to the server. Type 'exit' to end the chat.

## Communication

- The server listens for incoming connections and creates a new thread for each connected client.
- The client connects to the server and starts a separate thread to receive messages from the server.
- Messages are exchanged in real-time, and the chat can be terminated by typing 'exit'.
