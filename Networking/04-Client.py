import socket

s = socket.socket()

port = 9999

s.connect(('localhost', port))

# receive no more than 1024 bytes
data = s.recv(1024)

print(data)

s.close()
