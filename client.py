import socket
import sys
PORT = 5050
SERVER = "localhost"
HEADER = 128
FORMAT = 'utf-8'
DISCONNECT_MESSAGE  = "!DISCONNECT"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' *(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World")
input()
send("Hello Everyone")
input()
send("Hello")

send(DISCONNECT_MESSAGE)

