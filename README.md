# Ethical-Hacking-using-Socket-Programming

## Socket
Is one of the endpoint of two-way connection link between two programs running on the network. A socket is bound to a port number so
that TCP layer can identify the application to which the data is destined to be. An endpoint is a combination of IP address and port number.

## IP Address
It is an unique set of strings separated by full stops('.') such that two computer systems can communicate with each other using Internet
Protocol over the network. 
They are of two types:
```
                                                IP
                                              `    `
                                             `      `
                                            `        `
                                          Public    Private 
```
## Public IP
It is the IP address provided by the Internet Service Provider(ISP) like Jio, Vodaphone, Idea, Airtel

## Private IP
It is the IP address which is provided by different routers or wifi

### To check your IP address of the system type following command on terminal/command prompt
#### For Windows
``` ipconfig ```

#### For Linux/Mac
``` ifconfig ```

### To see IP address of any website like Google, Facebook etc...
#### Type following on your terminal/command prompt
` ping facebook.com `
` ping google.com `

### IP Address also classified into
```
                                                IP
                                              `    `
                                             `      `
                                            `        `
                                          Static    Dynamic 
```
### Static IP
These are the IP address of the servers or websites like IP address of Google is 172.217.163.174 and of facebook is 157.240.192.35
These are same throughout the same country but can change from country to country.

### Dynamic IP
Thses are the category of IP address which changes frequently
If you see your IP address using "ipconfig" and if you restart your system and you see that the IP is changed this time.

### Difference between IP and Port number
We can understand this difference better using an analogy
IP address is nothing but the address of the city or street while Port number is the address of out house in which we are living

suppose we are using Skype & Netflix in our system then how TCP layer will know to whom it has to deliver the data i.e. to which application(whether Skype or Netflix) it has to deliver a particular data, so using port number it can distinguish between one or more application where the data is to be delivered.  

### How does Socket works

` socket.socket() `

Using this command a socket will be created now we have to bind this socket to an IP address as well as a port number which can be
done using

`socket.bind(host, port)`

After binding the socket we will send the data to the client using the command

`socket.send()`

After this, the client will be sending the data so we will be listening it with the comamnd and will receive the data sent by the client

```socket.listen()```

```socket.recv()```

If conversation is over then we can close the connection using the command

`socket.close()`

All the steps are:
  - socket.socket()
  - socket.bind(host, port)
  - socket.send()
  - socket.listen()
  - socket.recv()
  - socket.close()
  
