import time
import os
s = 0
m = 0
h = 0
while(s<60):
	if(s==59):
		m += 1
		s = 0
	if(m==60):
		print("1 Hour have Passed")
		break
	a = "{}h:{}m:{}s".format(h,m,s)

	print(a)
	s += 1
	time.sleep(1)
	os.system('clear')

