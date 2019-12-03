from thread import start_new_thread
from socket import *

def handleClient(connectionSocket):
    while True:
        sentence = connectionSocket.recv(1024)
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
    
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while True:
	connectionSocket, clientAddress = serverSocket.accept()	
	print 'Client Address: ' + str(clientAddress)
	#Note: for question-2, replace this loop by the thread call	
    	#while True:		
        #	sentence = connectionSocket.recv(1024)
	#	print 'Get Message: ' + str(sentence) 
        #	capitalizedSentence = sentence.upper()
        #	connectionSocket.send(capitalizedSentence)
    	#connectionSocket.close()

	start_new_thread(handleClient,(connectionSocket,))
	 	############## 
