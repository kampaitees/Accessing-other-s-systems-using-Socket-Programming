import sys
import socket

#AF_INET reprsents that we are going to use IPv4version of Internet Protocol
#SOCK_STREAMrepresent that we are using TCP/IP as a Internet Protocol instead of UDP

try:

    #creating the socket with IPv4 version and TCP as protocol in transport layer
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket successfully created')

#raising an error while creating the socket
except socket.error as msg:
    print('Error in socket connection ', msg)

try:

    #getting the IPaddress of google using PING
    host = socket.gethostbyname('www.google.com')

#raising error if we get any problem in getting IP address of google
except socket.gaierror as msg:
    print('Error in getting host address')
    sys.exit()

#using Http as a port as it's port number is 80
port = 80

#connecting to the google server
s.connect((host, port))

print('The socket is successfully connected to google on IP address: ', host)