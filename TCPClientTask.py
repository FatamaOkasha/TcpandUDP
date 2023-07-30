#Name :Fatma Mohammed Abdelgafour  Okasha(20198064) ,Hadeel Ali Saleem Ataya (20198097)
#Dept:Bioinformatics
#Level : 3

from socket import *

serverIP = gethostname()
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))


while True:

    sentence = input('Enter message to send or type Exit to disconnect :')
    if sentence == "Exit":
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('Received message from server:',modifiedSentence.decode())
        print('Now you are disconnected from the server')
        break
    else:
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('Received message from server:', modifiedSentence.decode())
clientSocket.close()
