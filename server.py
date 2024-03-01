import socket
import threading
import time

PORT = 5050
SERVER = "localhost"
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE  = "!DISCONNECT"
PUT_MSG = "put"
GET_MSG = "get"
#gets the public IP address of this computer
#SERVER = socket.gethostyname(socket.getname()) 
ADDR = (SERVER,PORT)

server_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_1.bind(ADDR)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION]{addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            if msg == DISCONNECT_MESSAGE:
                connected = False
            conn.send("Msg Received".encode(FORMAT))
            #print(f"[{addr}] {msg}")
    conn.close()


def start():
    server_1.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        cl_conn, cl_addr = server_1.accept()
        thread = threading.Thread(target=handle_client,args=(cl_conn,cl_addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")


print(f"Starting Server at {ADDR}")
start()