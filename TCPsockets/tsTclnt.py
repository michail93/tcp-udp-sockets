import socket 

tcpCliSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcpCliSock.connect(("smtp.gmail.com", 25))

wait_ip=input("Enter the ip address of the tcp server\nfor example \"192.168.0.10\" : ")
wait_port=int(input("Enter the port number : "))

tcpCliSock.connect((wait_ip, wait_port))

while True:
	data=input("> ")
	data=data.encode("utf-8")
	#print(data)
	if not data:
		break
	tcpCliSock.send(data)
	data=tcpCliSock.recv(2048)
	if not data:
	    break
	print(data.decode())

print("close socket")
tcpCliSock.close()

