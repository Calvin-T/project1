import socket
import sys

"""Client program to connect to root and top level name servers"""
#python client.py rsHostname rsListenPort tsListenPort

rsHostName=""
rsListenPort = 0
tsListenPort = 0

# get command line arguments
if len(sys.argv) == 4:
    rsHostName = str(sys.argv[1])
    rsListenPort = int(sys.argv[2]) #TODO add a check to make sure int cast works
    tsListenPort = int(sys.argv[3])
    print(rsHostName)
    print(rsListenPort)
    print(tsListenPort)
else:
    print("Invalid Command Line Arguments")
    exit(1)

# socket to talk to rs server
try:
    rsSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: RS Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

rsServer_addr=socket.gethostbyname(rsHostName)
rsServer_binding=(rsServer_addr,rsListenPort)
rsSocket.connect(rsServer_binding)


# socket to talk to ts server, have to get address from rs server first
tsHostName = "localhost"  # for testing purposes, will get actual tsHostName from rs server
try:
    tsSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: TS Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

tsServer_addr = socket.gethostbyname(socket.gethostname())
tsServer_binding=(tsServer_addr, tsListenPort)
tsSocket.connect(tsServer_binding)


# enclose this in a while loop -> while iterating through file, close both sockets when done with file
# Receive data from the server
data_from_RSserver = rsSocket.recv(200)
print("[C]: Data received from  rs server: {}".format(data_from_RSserver.decode('utf-8')))

data_from_TSserver = tsSocket.recv(200)
print("[C]: Data received from ts server: {}".format(data_from_TSserver.decode('utf-8')))

# close the client socket
rsSocket.close()
tsSocket.close()
exit()
