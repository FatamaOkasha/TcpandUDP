#Name :Fatma Mohammed Abdelgafour  Okasha(20198064) ,Hadeel Ali Saleem Ataya (20198097)
#Dept:Bioinformatics
#Level : 3

from socket import *

serverIP=gethostname()
serverPort = 13000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("This message :", message.decode(),"\n", "is received from :",clientAddress)


# C:\Users\User\PycharmProjects\pythonProject4
