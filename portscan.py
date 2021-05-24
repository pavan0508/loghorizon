import socket
import time
import os
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def scan(ip,port):
	try:
		if s.connect((ip,port)):
			s.timeout(1)
			return "open"
			s.close()
	except:
		return "close"
def body(i):
	while(i!="x"):
		if i == "1":
			quick = (20,22,25,8080,4444,444)
			ip = input("Enter the IP address to scan:")
			if(ip.count(".") == 3):
				for i in quick:
					print("port{}:".format(i),scan(ip,i))
					time.sleep(.2)
				print("\n")
				break
			else:
				print("Please check Your IP address and enter again")
				time.sleep(3)
				body(i)
		elif i == "2":
			ip = input ("Enter the Ip Address to scan:")
			if(ip.count(".") == 3):
				n = int(input("Enter the range of ports to scan:"))
				for port in range(n):
					print("port{}:".format(port),scan(ip,port))
					time.sleep(.2)
				print("\n")
				break
			else:
				print("Please check Your IP address and enter again")
				time.sleep(3)
				body(i)
os.system("clear")
print(".....PORT SCANNER.....")
print("Select options:1. quick scan 2. range scan x-exit")
i = input("option:")
body(i)