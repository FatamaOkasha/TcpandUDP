#Name :Fatma Mohammed Abdelgafour  Okasha(20198064) ,Hadeel Ali Saleem Ataya (20198097)
#Dept:Bioinformatics
#Level : 3

from socket import *

serverIP = gethostname()
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP , serverPort))

serverSocket.listen(1)

print("Lisenting at ",serverSocket.getsockname())
connectionSocket, addr = serverSocket.accept()
print("The server now is connected to :", addr)
print("Socket connects between", serverSocket.getsockname(), "and ", addr)



while True:
    sentence = connectionSocket.recv(1024).decode()
    if sentence != "Exit":
        print("Received Message from Client :", sentence)
        RespondMsgServer = f"Your data was {len(sentence.upper().encode())} bytes "
        connectionSocket.send(RespondMsgServer.encode())

    else:
        print("Received Message from Client :", sentence)
        print("Reply sent ,Server socket closed")
        RespondMsgServer = "Disconnected"
        connectionSocket.send(RespondMsgServer.encode())
        connectionSocket.close()
        print("Listening at ", serverSocket.getsockname())
        break








