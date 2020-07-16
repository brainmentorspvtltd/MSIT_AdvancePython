import socket


def main():
    soc = socket.socket()
    host = "127.0.0.1"
    port = 8888

    soc.connect((host, port))

    print("Enter 'quit' to exit")
    message = input(" -> ")

    while message != 'quit':
        soc.sendall(message.encode('utf-8'))
        data = soc.recv(1024)
        print(data.decode())
        message = input(" -> ")

    soc.send(b'quit')


main()
