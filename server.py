# import socket
# import pickle

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 1234))

# s.listen(5)

# name = {1: "Hello", 2: "Bello"}
# msg = pickle.dumps(name)


# while True:
# 	clientsocket, address = s.accept()
# 	print(f"Connection from {address} established")
# 	# clientsocket.send(bytes("Welcome!", "utf-8"))
# 	clientsocket.send(msg)
# 	clientsocket.close()


import threading
import socket
import pickle

host = '127.0.0.1' #localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []
data = {}

current = 1

def broadcast(message):
	iteration = 0
	for client in clients:
		client.send(message)
		iteration += 1

def handle(client, nickname):
	while True:
		itt = 0
		for clientx in clients:
			clientx.send(str(data[nicknames[itt]]).encode("ascii"))
			itt += 1
		try:
			message = client.recv(1024)
			if(data[nickname]['order'] == current):
				broadcast(message)
			else:
				broadcast(message + " INVALID".encode("ascii"))
		except:
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast(f'{nickname} has left the chat'.encode('ascii'))
			nicknames.remove(nickname)
			break

def receive():
	while True:
		client, address = server.accept()
		print(f"Connected with {str(address)}")

		client.send("NICK".encode("ascii"))
		nickname = client.recv(1024).decode("ascii")

		nicknames.append(nickname)
		clients.append(client)
		data[nickname] = {"money": 1500, "properties": [], "utilities": [], "gotojail": 0, "order": len(clients)}


		print(f"Nickname of client is {nickname}")
		broadcast(f'{nickname} has joined the chat'.encode('ascii'))
		client.send("Connected to the server!".encode('ascii'))
		thread = threading.Thread(target=handle, args=(client, nickname))
		thread.start()


print("Server is listening...")
receive()