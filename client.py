import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Importing the socket
s.connect(("192.168.59.121",8080))#Example of Ip address
while True:
    data=input("EnterThe message from sender: :").encode()
    s.sendall(data) #To send all data to the user