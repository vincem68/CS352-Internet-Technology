import threading
import time
import random

import socket

def client():
	try:
		cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[C]: Client socket created")
	except socket.error as err:
		print('socket open error: {} \n'.format(err))
		exit()

	#Define the port on which you want to connect to the server
	port = 50007
	localhost_addr = socket.gethostbyname(socket.gethostname())
	
	#Connect to the server on local machine
	server_binding = (localhost_addr, port)
	cs.connect(server_binding)

	fd = open('in-proj0.txt', 'r')
	fd_output = open('out-proj0.txt', 'w')
	file_line = fd.readline()
	while file_line:
		print("[C]: Data sent to server:\n" + file_line)
		cs.send(file_line.encode('utf-8'))
		data_from_server = cs.recv(1024)
		new_string = data_from_server.decode('utf-8')
		fd_output.write(new_string)
		print("[C]: Data received from server:\n" + new_string)
		file_line = fd.readline()
	fd.close()
	fd_output.close()

	
	# close the client socket
	cs.close()
	exit()

	
if __name__ == "__main__":
	t2 = threading.Thread(name='client', target=client)
	t2.start()
	print("Done.")
