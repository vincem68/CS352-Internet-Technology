1. The program has both the server and client methods create sockets and creates a 
connection between each other. Once the connection has been established, the server 
creates a message and sends the data to the client over the connection and the 
client receives and displays it.

2. We see that after running it again immediately the time it takes for the server to 
connect to the client is different. This is because there is a sleep function that randomly 
picks between 1 and 5 seconds after the server code starts before the client code runs. 
When we remove the sleep()s, the code executes both the server code and the client code 
immediately after and there is no wait.

Project explanation:
The client opens a file under the name in-proj0.txt and reads each line at a time. From 
there, it stores each line from the file in a string and sends the string to the server. 
The server receives the string, creates a new string which is the reversed received 
string and combines the two strings together. The client then receives the string and 
writes it to a file named out-proj0.txt. This continues until every line in in-proj0.txt
is read.
