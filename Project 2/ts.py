import threading
import socket
import sys

class Node:
	def __init__(this_node, domain, IP_addr, next_node, flag):
		this_node.domain = domain
		this_node.IP_addr = IP_addr
		this_node.next_node = next_node
		this_node.flag = flag


def ts():

	ts_dns_table_head = None
	tsListenPort = None
	if len(sys.argv) == 2:
		tsListenPort = int(sys.argv[1])
	fd = open('PROJI-DNSTS.txt', 'r')
	file_line = fd.readline()
	while file_line:
		space = -1
		index = 0
		for letter in file_line:
			if letter == ' ':
				space = index
				break
			else:
				index += 1
		domain_name = file_line[0: space]
		space_2 = -1
		index = 0
		second_line = file_line[(space + 1) : ]
		for letter in second_line:
			if letter == ' ':
				space_2 = index
				break
			else:
				index += 1
		IP_address = second_line[0 : space_2]
		third_line = second_line[(space_2 + 1) : ]
		index = 0
		space_3 = -1
		for letter in third_line:
			if letter == ' ':
				space_3 = index
				break
			else:
				index += 1
		flag = third_line[0 : space_3]
		new_node = Node(domain_name, IP_address, None, flag)
		current_node = ts_dns_table_head
		if current_node == None:
			ts_dns_table_head = new_node
		else:
			while current_node.next_node != None:
				current_node = current_node.next_node
			current_node.next_node = new_node
		file_line = fd.readline()
	
	fd.close()
	try:
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as err:
		print("Socket open error: {}\n".format(err))
		exit()
	server_binding = ('', tsListenPort)
	server_socket.bind(server_binding)
	server_socket.listen(1)
	host = socket.gethostname()
	local_host_ip = (socket.gethostbyname(host))
	client_sockid, address = server_socket.accept()
	data_from_client = client_sockid.recv(1024)
	while data_from_client:
		client_line = data_from_client.decode('utf-8')
		end = len(client_line) - 1
		client_line = client_line[0 : end]
		current_node = ts_dns_table_head
		sent = False
		while current_node != None:
			if current_node.domain.lower() == client_line.lower():
				sent = True
				ts_reply = current_node.domain + ' ' + current_node.IP_addr + ' ' + current_node.flag	
				client_sockid.send(ts_reply.encode('utf-8'))
				break
			current_node = current_node.next_node
		if sent == False:
			error_message = client_line + ' ' + '- Error:HOST NOT FOUND'
			client_sockid.send(error_message.encode('utf-8'))
		data_from_client = client_sockid.recv(1024)


	server_socket.close()	
	exit()

if __name__ == '__main__':
	thread_3 = threading.Thread(name='ts', target=ts)
	thread_3.start()
