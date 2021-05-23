import os
import time
os.system("clear")
t = int(input("Enter the Time to ShutDown:"))
for i in range(t):
	print(i)
	os.system("clear")
	time.sleep(1)
print("Shutting Down....")
time.sleep(2)
os.system("shutdown now")
