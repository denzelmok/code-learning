from socket import *
import requests
import sys


#print("What is the server IP?")
serverName = sys.argv[1]
#print("What is the server port?")
serverPort = sys.argv[2]
serverPort = int(serverPort)
try:
	#print("What is the file name?")
	filename = sys.argv[3]
	filepath = 'http://'+serverName+':'+str(serverPort)+'/'+filename
	print(filepath)
	r = requests.get(filepath)
	print(r.text)
	clientSocket = socket(AF_INET,SOCK_STREAM)
	clientSocket.connect((serverName,int(serverPort)))
	clientSocket.close()
except IOError:
	print("404 Not Found")
	sys.exit(1)
clientSocket.close()
print ("TCP client completed - exiting")
