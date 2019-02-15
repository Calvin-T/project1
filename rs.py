import socket


RS_DNS_Table = {}

def populateData(filename):
	lines = [line.rstrip('\r\n') for line in open(filename)]
	for line in lines:
		lineSplit = line.split()
		RS_DNS_Table[lineSplit[0]] = [lineSplit[1],lineSplit[2]]
		
	print(RS_DNS_Table)

if __name__ == '__main__':
	populateData("PROJI-DNSRS.txt")