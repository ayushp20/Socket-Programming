import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))

print("Connected to chat server...")

while True:
	msg_in = s.recv(1024)
	msg_in = msg_in.decode()
	print("SERVER : ", msg_in)
	msg = input(str("Client ->"))
	msg = msg.encode()
	s.send(msg)
	print("Message sent successfully.") 