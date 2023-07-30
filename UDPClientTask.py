#Name :Fatma Mohammed Abdelgafour  Okasha(20198064) ,Hadeel Ali Saleem Ataya (20198097)
#Dept:Bioinformatics
#Level : 3

from socket import *
import sys

FileName=""
ClientPortNumber=0
ClientMessage=""

if len(sys.argv) > 1:
 FileName=sys.argv[0]
 ClientPortNumber=int(sys.argv[1])
 ClientMessage=sys.argv[2]

serverIP =gethostname()
serverPort = 13000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind((serverIP,ClientPortNumber))

clientSocket.sendto(ClientMessage.encode(), (serverIP, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

clientSocket.close()


