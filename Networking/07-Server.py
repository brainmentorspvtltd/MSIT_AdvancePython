import socket
from threading import Thread
import sys
import traceback


def start_server():
    host = "127.0.0.1"
    port = 8888

    soc = socket.socket()
    print("Socket created")

    try:
        soc.bind((host, port))
    except:
        print("Bind failed, error : ", sys.exc_info())

    soc.listen(5)
    print("Socket listening")

    while True:
        connection, address = soc.accept()
        ip, port = address[0], address[1]
        print("Connected with ", ip, ":", port)
        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            print("Thread did not start")
            traceback.print_exc()

    soc.close()


def client_thread(connection, ip, port, max_buffer_size=5120):
    is_active = True

    while is_active:
        client_input = receive_input(connection, max_buffer_size)
        if "QUIT" in client_input:
            print("Client is requesting to quit")
            connection.close()
            print("Connection ", ip, ":", port, "closed")
            is_active = False
        else:
            print("Processed message : ", client_input)
            msg = input(" -> ")
            connection.sendall(msg.encode('utf-8'))


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)

    if client_input_size > max_buffer_size:
        print("The input size is greater than expected - ", client_input_size)

    decoded_input = client_input.decode('utf-8')
    result = process_input(decoded_input)

    return result


def process_input(decoded_input):
    print("Processing the input received from client")
    return decoded_input.upper()


start_server()
