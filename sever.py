import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#impoting the sockets
s.bind(("192.168.59.178",4000))
#listening to the socket
s.listen()
con,addr=s.accept()
while True:
    data=con.recv(1024)
    d=data.decode()
    print(data)