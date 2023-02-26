0. Name: Vincent Mandola  netID: vam91

1. The client creates a socket to the rs server and reads a hostname from the file and sends each name to rs one by one.
The rs server goes through the linked list and checks to see if the hostname exists, and sends back the IP address if it
does. If the name is not there, the rs server sends back the hostname of the ts server and the client creates a socket and 
connects to the ts server to find the IP address.

2. Every function of the code works.

3. Issues I faced from this project were trying to have the client connect to the ts server as the connection refused
a lot of the time, having the servers not correctly find host names that were in its DNS table, and having some fields
in RESOLVED.txt missing.

4. I learned more about how sockets work, such as how certain functions work like gethostbyname() and fully understanding
how sockets work using what parameters are given to needed functions and how a client program can communicate with a server.
