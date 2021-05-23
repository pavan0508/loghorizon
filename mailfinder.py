import re
import os
os.system("clear")

print(".......Emails Finder.......")
# for python version 2.7 use raw_input() otherwise use input()
t = input("Enter the file name or  path:")
print("\n")
f = open(t,"r")
email = re.findall(r"[\w.-]+@[\w]+.com",f.read())
i = 0
try:
	for emails in email:
		i += 1
		print("{}.{}".format(i,emails))
except:
	print("No Emails found in {}".format(t))
