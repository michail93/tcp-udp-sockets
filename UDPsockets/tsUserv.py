import socket 
from time import ctime


udpSerSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSerSock.bind(("192.168.0.28", 21567))

while True:
	print("waiting for message...")
	data, addr=udpSerSock.recvfrom(1024)
	# print(addr)
	sendmessage=" [{}] {}".format(ctime(), data)
	sendmessage=sendmessage.encode()
	udpSerSock.sendto(sendmessage, addr)
	print("...received from and returned to: ", addr, "message: ", data)
udpSerSock.close()	
