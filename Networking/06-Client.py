import socket


def main():
    host = "192.168.0.102"
    port = 5000

    mysocket = socket.socket()
    mysocket.connect((host, port))

    message = input(" -> ")

    while message != 'q':
        mysocket.send(message.encode())
        data = mysocket.recv(1024).decode()

        print("Received from server: ", data)

        message = input(" -> ")

    mysocket.close()


main()
