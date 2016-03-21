#!/usr/local/bin/python
from socket import *
serverName = 'localhost'
serverPort = 15011
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message = input('Input lowercase sentences: ')
    if (message=="quit"):
        break
    clientSocket.sendto(bytes(message, 'UTF-8'),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage)
clientSocket.close()
