from socket import * 
import sys 

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverAddr = '163.143.11.126'

# Bind the socket to server address and server port, then listen
serverSocket.bind((serverAddr, serverPort))
serverSocket.listen(1)


while True:
	print('The server is ready to receive')
	print(serverAddr)

	# Set up a new connection from the client
	connectionSocket, clientAddress = serverSocket.accept()

	#try:
		# Receives the request message from the client
		message = connectionSocket.recv(1024).decode('utf-8')  #should have .decode()
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read() 	# Store the file in a temporary buffer
		# Send the HTTP response header line to the connection socket
		connectionSocket.send('HTTP/1.1 200 OK') # don't need .encode() here 
 
		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			print(outputdata[i]) # each time send outputdata[i]

		connectionSocket.send("\r\n") 
		connectionSocket.close()


serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data

	
