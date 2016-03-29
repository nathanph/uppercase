#!/usr/bin/python3
from socket import *
from threading import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5)

def uppercase(connection_socket):
    while True:
        sentence = connection_socket.recv(1024)
        capitalized_sentence = sentence.upper()
        connection_socket.send(capitalized_sentence)
    connection_socket.close()

print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    # Thread here.
    thread = Thread(target=uppercase, args=(connectionSocket,))
    thread.start()


# while True:
#     sentence = connectionSocket.recv(1024)
#     capitalizedSentence = sentence.upper()
#     connectionSocket.send(capitalizedSentence)
# connectionSocket.close()


