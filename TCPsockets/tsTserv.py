import socket
import time

tcpSerSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Example : 192.168.0.28 - Your IP address in the subnet
# 22567 - Port number
tcpSerSock.bind(("192.168.0.28", 22567))
tcpSerSock.listen(5)

while True:
	print("waiting for connection...")
	tcpCliSock, addr=tcpSerSock.accept()
	print("connected from: {}".format(addr))
	while True:
		print("Accept the message")
		data=tcpCliSock.recv(1024)
		data=data.decode()
		if data=="stop server":
			print("server stopped")
			break
		print(data)
		if not data:
			break
		sendmessage=" [ {} ]  {}".format(time.ctime(), data)
		sendmessage=sendmessage.encode()		
		tcpCliSock.send(sendmessage)
	tcpCliSock.close()
	if data=="stop server":
		break
tcpSerSock.close()			
