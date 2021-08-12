# import socket
# import pickle

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostname(), 1234))

# while True:
# 	msg = s.recv(1024)
# 	# print(msg.decode('utf-8'))
# 	if(len(msg) > 0):
# 		msg = pickle.loads(msg)
# 		print(msg)

# 	

import socket
import threading
import pickle
import traceback

nickname = input("Choose a nickname: ")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			try:
				data = eval(message)
				print("Money", data['money'])
				
			except:
				# traceback.print_exc()
				if message == 'NICK':
					client.send(nickname.encode('ascii'))
				else:
					print(message)
				


		except:
			traceback.print_exc()
			print("An error has occured")
			client.close()
			break

	
def write():
	while True:
		msg = input('')
		print("\033[A                             \033[A")
		message = f"{bcolors.FAIL + nickname + bcolors.ENDC}: {msg}"
		client.send(message.encode("ascii"))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()