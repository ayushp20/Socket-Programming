import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

print("Server started on host :  ", host)

s.bind((host, port))

print("Server completed binding of host and port successfully.")

s.listen(1)
print("Server now waiting for incoming connections...")

clientsocket, addr = s.accept()
print(addr, "has connected to this server.")

while True:
	msg = input(str("Server -> "))
	msg = msg.encode()
	clientsocket.send(msg)
	print("Message sent.")

	msg_in = clientsocket.recv(1024)
	msg_in = msg_in.decode()
	print("Client : ", msg_in)
