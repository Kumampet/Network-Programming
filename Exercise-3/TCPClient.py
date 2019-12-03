from socket import *
import time

start_time = time.time()

serverName = 'www.playstation.com'
serverPort = 80
destAddress = (serverName,serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(destAddress)
#while True:
#sentence = raw_input('Input lowercase sentence:')
sentence = "GET / HTTP/1.1\r\nHost: www.playstation.com\r\n\r\n"
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print (modifiedSentence)
d = time.time() - start_time
print('Delay: %f sec' %(d))
clientSocket.close()
