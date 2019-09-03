import sys
import socket

#creating a socket having IP version as IPv4 and TCP/IP as working protocol in Transport layer 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Initilizing host to out IP address and port number as 9999
host = '10.53.125.187'
port = 9999
count = 0
#connecting to the socket by combining IP address and port
s.connect((host, port))

while count < 20:
    cmd = input("Enter message to be delivered:\n")
    if cmd == 'Bye':
        break
    #sending some message to the server
    s.send(str.encode(cmd))

    #storing the information sent by the server
    msg = s.recv(1024).decode()
    print(msg)
    count += 1
