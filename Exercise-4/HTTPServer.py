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

	try:
		# Receives the request message from the client
		message = connectionSocket.recv(1024).decode('utf-8')  #should have .decode()
		#print(message)
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = message.split()[1]
		#print(filename)
		f = open(filename[1:])
		outputdata = f.read() 	# Store the file in a temporary buffer
		# Send the HTTP response header line to the connection socket
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n') # don't need .encode() here 
 		# Send the content of the requested file to the connection socket
		#print(outputdata)
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i:i+1]) # each time send outputdata[i]
		connectionSocket.send("\r\n") 
		connectionSocket.close()

	except IOError:
        	#Send response message for file not found 
        	connectionSocket.send('\nHTTP/1.1 404 Not Found\r\n\r\n')
        	errorMessage = '<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n'
        	connectionSocket.send(errorMessage)
        	connectionSocket.send(b'\r\n\r\n')
        

connectionSocket.close()

serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data

	
