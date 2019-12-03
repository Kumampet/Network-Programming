from socket import *

serverName = '163.143.11.127' # IP address of your server
serverPort = 12000  # Port number of your server
destAddress=(serverName,serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)

print("-----------------------")
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),destAddress)
print("Sent message: " + message)
receivedMessage, serverAddress = clientSocket.recvfrom(2048)
print("Received message: " + receivedMessage.decode())
