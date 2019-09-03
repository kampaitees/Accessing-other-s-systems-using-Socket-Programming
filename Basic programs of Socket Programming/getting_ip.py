import socket
ip_google  = socket.gethostbyname('www.google.com')
ip_fb  = socket.gethostbyname('www.facebook.com')
ip_amazon  = socket.gethostbyname('www.amazon.com')
print('Ip Address of Google is: ', ip_google)
print('Ip Address of Facebook is: ', ip_fb) 
print('IP Address of Amazon is: ', ip_amazon)