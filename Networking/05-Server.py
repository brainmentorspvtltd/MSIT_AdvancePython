import socket


def main():
    host = "192.168.0.102"
    port = 5000

    mysocket = socket.socket()
    mysocket.bind((host, port))

    print("Server started on", port)
    print("Waiting for connection...")

    mysocket.listen(1)
    conn, addr = mysocket.accept()
    print("Connection from", addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: ", data)

        data = input("Enter message: ")
        print("sending: ", data)
        conn.send(data.encode())

    conn.close()


main()
