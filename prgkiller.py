import os
import time
print(os.getcwd())
print(os.system("ls -al"))
t = input("give the time to delete the program")
n = 1
while(n<t):
	if(n==t-1):
		os.system("clear")
		os.system("rm -f a2.py")
		print("deletd")
	n += 1
	time.sleep(1)
