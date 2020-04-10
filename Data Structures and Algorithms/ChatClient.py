import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket.connect(('127.0.0.1', 8000))
while 1:
    data = input(">")
    clientsocket.send(data.encode())
    if not data:
        break
    newdata = clientsocket.recv(1024)
    print("Received from sever: ", repr(newdata))
clientsocket.close()
