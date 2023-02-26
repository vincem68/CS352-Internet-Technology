import socket
import threading
import sys

def client():
	
	rsHostName = sys.argv[1]
	rs_port = int(sys.argv[2])
	ts_port = int(sys.argv[3])
	try:
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as err:
		print('socket open error: {} \n'.format(err))
		exit()

	host_address = socket.gethostbyname(rsHostName)
	server_binding = (host_address, rs_port)
	client_socket.connect(server_binding)

	
	fd = open('PROJI-HNS.txt', 'r')
	fd_2 = open('RESOLVED.txt', 'w')
	
	file_line = fd.readline()
	ts = False
	while file_line:
		file_line = file_line.lower()
		client_socket.send(file_line.encode('utf-8'))
		reply_from_server = client_socket.recv(1024)
		server_message = reply_from_server.decode('utf-8')
		space = 0
		index = 0
		for letter in server_message:
			if letter == ' ':
				space += 1
				if space == 2:
					index += 1
					break
			index += 1
		flag = server_message[index : ]
		if flag == 'A':
			server_message += '\n'
			fd_2.write(server_message)
		else:
			if ts == False:
				try:
					client_socket_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				except socket.error as err:
					print('socket open error: {} \n'.format(err))
					exit()
				end = 0
				for letter in server_message:
					if letter == ' ':
						break
					end += 1
				tsHostName = server_message[0 : end]
				host_address_2 = socket.gethostbyname(tsHostName)
				server_binding_2 = (host_address_2, ts_port)
				client_socket_2.connect(server_binding_2)
				client_socket_2.send(file_line.encode('utf-8'))
				reply_from_server_2 = client_socket_2.recv(1024)
				server_message_2 = reply_from_server_2.decode('utf-8')
				server_message_2 += '\n'
				fd_2.write(server_message_2)
				ts = True
			else:
				client_socket_2.send(file_line.encode('utf-8'))
				reply_from_server_2 = client_socket_2.recv(1024)
				server_message_2 = reply_from_server_2.decode('utf-8')
				server_message_2 += '\n'
				fd_2.write(server_message_2)
		file_line = fd.readline()

	client_socket.close()
	client_socket_2.close()
	fd.close()
	fd_2.close()

if __name__ == "__main__":
	thread_2 = threading.Thread(name='client', target=client)
	thread_2.start()
