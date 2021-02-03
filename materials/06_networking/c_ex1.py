#!usr/bin/python
import sys
import socket


# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((socket.gethostname(), 1234))

# msg = client_socket.recv(1024)
# print(msg.decode("utf-8"))
# welcome_msg = client_socket.send(bytes("Pozdrav na server!", "utf-8"))

# my_username = input("Username:")

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((socket.gethostname(), 1234))
# client_socket.setblocking(False)

# # username = my_username.encode('utf-8')
# # username = my_username
# username_header = f"{len(my_username):<10}"
# # username_header = f"{len(username):<10}".encode('utf-8')
# client_socket.send(bytes(username_header + my_username, "utf-8"))

# while True:
    # message = input(f'{my_username} > ')
    # if message:
        # # message = message.encode('utf-8')
        # message_header = f"{len(message):<10}"
        # client_socket.send(bytes(message_header + message, "utf-8"))

my_username = input("Username:")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 1234))
client_socket.setblocking(False)

username_header = f"{len(my_username):<10}"
client_socket.send(bytes(username_header + my_username, "utf-8"))

while (message := input(f'{my_username} > ')):
    message_header = f"{len(message):<10}"
    client_socket.send(bytes(message_header + message, "utf-8"))
    try:
        while True:
            username_header = client_socket.recv(10)
            if not len(username_header):
                print("Server ukoncen")
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(10)
            message_length = int(message_header.decode('utf-8').strip())
            print(f"{username} > {client_socket.recv(message_length).decode('utf-8')}")

    except IOError:
        continue
