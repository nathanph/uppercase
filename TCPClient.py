#!/usr/bin/python3
from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:
    sentence = input('Input lowercase sentence: ')
    if(sentence=="quit"):
        clientSocket.shutdown(SHUT_RDWR)
        clientSocket.close()
        break;
    clientSocket.send(bytes(sentence, 'UTF-8'))
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence)

