from socket import *

serverName = '163.143.3.68' # IP address of your server
serverPort = 12000  # Port number of your server
destAddress=(serverName,serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)
n = 1

while True:
	if(n>9):
     	        print "Over 9 time! Breaked!"
		break
	print '-----------------------'
	message = raw_input('Input lowercase sentence:')
	clientSocket.sendto(message,destAddress)
	print str(n) + ': Sent message: ' + str(message)
	receivedMessage, serverAddress = clientSocket.recvfrom(2048)
	print str(n) + ': Received message: ' + str(receivedMessage)
	n+=1

