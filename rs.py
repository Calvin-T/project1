import socket
import sys

"""Root level name server program"""

RS_DNS_Table = {}

def populateData(filename):
	lines = [line.rstrip('\r\n') for line in open(filename)]
	for line in lines:
		lineSplit = line.split()
		RS_DNS_Table[lineSplit[0]] = [lineSplit[1],lineSplit[2]]
		
	print(RS_DNS_Table)

if __name__ == '__main__':
	populateData("PROJI-DNSRS.txt")
	

rsListenPort = 0
if len(sys.argv) == 2:
    #check that this is an integer, make sure that it is non-neg
    try:
        rsListenPort = int(sys.argv[1])
    except ValueError:
        exit(1)

else:
    # error, too many or too few command line args-> exit()
    exit(1)

server_binding = ('', rsListenPort) #50007
serverSocket.bind(server_binding)
serverSocket.listen(1)
host = socket.gethostname()
print("[S]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[S]: Server IP address is {}".format(localhost_ip))
csockid, addr = serverSocket.accept()
print("[S]: Got a connection request from a client at {}".format(addr))

# send a intro message to the client.
msg = "Connected to RS server"
csockid.send(msg.encode('utf-8'))
#then wait for queries
#have a closing protocol
#client finishes, send an exit message to server, then server will call close()

# Close the server socket
serverSocket.close()
exit()
