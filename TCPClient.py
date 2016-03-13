#!/usr/local/bin/python
from socket import *
serverName = 'localhost'
serverPort = 15011
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentences: ')
clientSocket.sendto(bytes(message, 'UTF-8'),(serverName, serverPort))
modifiedMessage, serverAddrfess = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()
