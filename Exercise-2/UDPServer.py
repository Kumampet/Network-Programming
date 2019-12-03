from socket import *

serverPort = 12000 # Port number of your server
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive!"
n = 1

while True:
	print '-----------------------'
	receivedMessage,clientAddress = serverSocket.recvfrom(2048)
	print str(n) + ': Received message: ' + str(receivedMessage)
	print str(n) + ': Client Address' + str(clientAddress)
	modifiedMessage = receivedMessage.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)
	print str(n) + ': Sent message: ' + str(modifiedMessage)
	n += 1

    
