import socket

# ip = socket.gethostbyname("www.google.com")
# print(ip)

try:
    s = socket.socket()
    print("Socket successfuly created")
except socket.error as err:
    print("Err : ", err)

# default port
port = 80

try:
    host_ip = socket.gethostbyname("www.google.com")
    # get address information error - internet is down
except socket.gaierror:
    print("Error occured")

s.connect((host_ip, port))

print("Successfuly connected to google using host_ip - ", host_ip)
