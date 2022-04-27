"""
This program represents the server host's interface for local/external communication.

Author: Ricardo Y. Rodriguez Gonzalez
Student ID: 802-18-2754
"""
# This code was implemented from Telusko's base code and explanation at https://youtu.be/u4kr7EFxAKk"

from full_lexer import lexer
import socket

PORT = 9999
BUFF = 1048
local_server = 'localhost'


def server(address):
    # IPv4 - TCP by default
    server_socket = socket.socket()

    print('SOCKET HAS BEEN CREATED.\n')

    # test_address = input("Default Communication: Local\nFor external connection enter your IP Address.\n\nEnter address: ")

    # if address != "":
    #     server_socket.bind((address, PORT))
    #     print(f"Binding address: {address}... \n")
    # else:
    #     server_socket.bind((address, PORT))
    #     print("Binding local server... \n")

    server_socket.bind((address, PORT))
    print("Binding local server... \n")
    server_socket.listen()

    # connections = input("Enter the number of connections: ")
    # print(f"Waiting for {connections} connections...\n")
    print("Waiting for connection...\n")

    client_socket, address = server_socket.accept()  # Receive Address

    print(f"Connected with: {address}")

    data = client_socket.recv(BUFF).decode()
    print(f"\nData received: {data} from {address}.\n")

    lexer.input(data)  # Receive data to tokenize

    # tokenization
    while True:
        t = lexer.token()
        if not t:
            break
        print(f"Data Sent: {t}")
        client_socket.send(bytes(str(t), 'utf-8'))  # Send tokenized version of data

    client_socket.close()
    print("\nSOCKET CLOSED")
