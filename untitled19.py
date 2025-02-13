# -*- coding: utf-8 -*-
"""untitled19.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/preethignanasekhar/dcebd41c17dd25c0d53abd310f810f15/untitled19.ipynb
"""

import socket

HOST = 'localhost'
PORT = 8888

# Create and bind the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server is listening on {HOST}:{PORT}")

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Client connected: {client_address}")

    try:
        # Receive the file name
        file_name = client_socket.recv(1024).decode()
        print(f"Receiving file: {file_name}")

        # Open a file for writing in binary mode
        with open(file_name, 'wb') as file:
            while True:
                # Receive data in chunks
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)

        print(f"File '{file_name}' received successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()