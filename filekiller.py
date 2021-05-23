import os
import time
print(os.getcwd())
print(os.system("ls -al"))
t = input("give the time to delete the program")
f = input("name of the file U want to Delete?")
n = 1
while(n<t):
	if(n==t-1):
		os.system("clear")
		os.system("rm -f {}".format(f))
		print("deletd")
	n += 1
	time.sleep(1)
