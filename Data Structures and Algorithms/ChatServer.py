import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(('127.0.0.1', 8000))
serversocket.listen(1)
clientsocket, clientaddress = serversocket.accept()
print('Connection from', clientaddress)

while True:
    data = clientsocket.recv(1024)
    if not data:
        break
    print("Received from client: ", data.decode())
    print("Echo:", repr(data))
    clientsocket.send(data)
clientsocket.close()
serversocket.close()
