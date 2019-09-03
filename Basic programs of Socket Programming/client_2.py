import sys
import socket

#creating a socket having IP version as IPv4 and TCP/IP as working protocol in Transport layer 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Initilizing host to out IP address and port number as 9999
host = '192.168.43.34'
port = 9999

#connecting to the socket by combining IP address and port
s.connect((host, port))

#sending some message to the server
s.send(str.encode("Please tell me today's date"))

#storing the information sent by the server
date = s.recv(1024).decode()

#printing the date sent by the server
print("Today's date is: ", date) 

#receiving final message from the server and printing it
final_msg = s.recv(1024).decode()
print(final_msg)

s.send(str.encode("Bye, see you soon!"))