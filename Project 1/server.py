import threading
import time
import random
import socket

def server():
	try:
		ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[S]: Server socket created")
	except socket.error as err:
		print('socket open error: {}\n'.format(err))
		exit()

	server_binding = ('', 50007)
	ss.bind(server_binding)
	ss.listen(1)
	host = socket.gethostname()
	print("[S]: Server host name is {}".format(host))
	localhost_ip = (socket.gethostbyname(host))
	print("[S]: Server IP address is {}".format(localhost_ip))
	csockid, addr = ss.accept()
	print ("[S]: Got a connection request from a client at {}".format(addr))
	
	#send a intro message to the client.
	data_from_client = csockid.recv(1024)
	while data_from_client:
		file_line = data_from_client.decode('utf-8')
		reverse_string = ""
		y = len(file_line) - 1
		while y >= 0:
			reverse_string += file_line[y]
			y -= 1
		full_line = reverse_string + file_line
		full_line = full_line[1:]
		csockid.send(full_line.encode('utf-8'))
		data_from_client = csockid.recv(1024)


	# Close the server socket
	ss.close()
	exit()

if __name__ == "__main__":
	t1 = threading.Thread(name='server', target=server)
	t1.start()
