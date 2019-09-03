import sys
import socket

#creating a socket having IP version as IPv4 and TCP/IP as working protocol in Transport layer 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Initilizing host to out IP address and port number as 9999
host = '192.168.43.34'
port = 9999

#connecting to the socket by combining IP address and port
s.connect((host, port))


#receiving final message from the server and printing it
final_msg = s.recv(1024).decode()
print(final_msg)