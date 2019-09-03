import sys
import socket
from datetime import date

#Initilizing host to empty as we want to listen from any system not a particluar system and port number as 9999
host, port, count = '', 9999, 0
try:

    #creating a socket having IP version as IPv4 and TCP/IP as working protocol in Transport layer 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket is created successfully!')

#if we get any error then message will be printed so it is easy to debug that bug is in this part of code
except socket.error as msg:
    print('Connection error: ', str(msg))

try:

    #binding IP address & port to the socket
    s.bind((host, port))
    print('Socket is binded successfully!')

    #number inside listen specifies number of unaccepted connections that system will allow before refusing new connections
    s.listen(5)
 
#if we get any error then message will be printed so it is easy to debug that bug is in this part of code
except socket.error as msg:
    print('Socket Binding error: ', str(msg))


#accepting connection
conn, address = s.accept()
print('Connection has been established! |'+' IP '+address[0]+' | Port '+str(address[1]))

while count < 20:

    msg = conn.recv(1024).decode()
    print(msg)

    if cmd == 'Bye':
        break

    cmd = input("Enter message to be delivered\n")
    conn.send(str.encode(cmd))
    count += 1

#closing connection with client
conn.close()
s.close()
sys.exit()
