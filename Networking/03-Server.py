# Server
import socket

# create socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer
port = 9999

# now bind the server to this port
s.bind(('localhost', port))
print("Socket binded to ", port)

# put the socket in listening mode
s.listen(5)
# 5 here means that 5 connections are kept waiting if the server is busy and a 6th connection tries to connect then that connection is refused
print("Socket is listening")

message = "Thankyou for connecting"

while True:
    # accept connection from client
    c, addr = s.accept()
    print("Got connection from ", addr)

    # send a message to the client
    c.send(message.encode("utf-8"))

    # close the connection
    c.close()
