"""
This program represents a client's interface for local/external communication.

Author: Ricardo Y. Rodriguez Gonzalez
Student ID: 802-18-2754
"""
# This code was implemented from Telusko's base code and explanation at https://youtu.be/u4kr7EFxAKk"

import socket

PORT = 9999
BUFF = 1048
local_server = 'localhost'


def client(address):

    # IPv4 - TCP by default
    client_socket = socket.socket()

    print('SOCKET HAS BEEN CREATED.\n')

    # address = input("Default Communication: Local\nFor external connection enter your IP Address.\n\nEnter address: ")

    # if address != "":
    #     client_socket.connect((address, PORT))
    #     print(f"Connecting to {address}... \n")
    # else:
    #     client_socket.connect((local_server, PORT))
    #     print("Connecting to local host... \n")

    client_socket.connect((address, PORT))
    print("Connecting local server... \n")

    client_socket.send(bytes(input("Enter the data to be tokenized: \n"), 'utf-8'))

    while True:
        data = client_socket.recv(BUFF).decode('utf-8')
        if len(data) <= 0:
            break
        print(f"Data Received: {data}")  # Prints tokenized input

    client_socket.close()
    print("\nSOCKET CLOSED")
