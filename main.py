"""
This Program is the runs the lexer to tokenize values of a function.
This is my own Programming Language using PLY.

Author: Ricardo Y. Rodriguez Gonzalez
Student ID: 802-18-2754
"""
from my_lexer import lexer
from my_parser import parser
from client import client
from server import server

# Insert file name:
"""
file = open('test2', 'r')  # opens the file
lexer.input(file.read())  # reads every line of the file
"""

# Hard Codded Input:

# data = 'my_func(x, y)'


data = 'communicate(destination, origin)'

print(f"Test Data: {data}\n")
lexer.input(data)

# tokenization
while True:
    t = lexer.token()
    if not t:
        break
    print(t)


# file.close()  # closes the file
#######################################################################################################################

# def communicate(destination, origin):
#     server(destination)
#     client(origin)


# communicate('localhost', 'localhost')
