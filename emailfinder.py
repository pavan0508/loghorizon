import os
import re
#To find the email id in a list which is in a file
storage = [] #This list is for storing the emails after extraction from the file.
while True:
    try:    
        target_file = input("Give the Path to the file where emails are located:")
        f = open(target_file,'r')
        emails = re.findall(r'\w+@\w+.com',f.read())
        f.close()
        break
    except Exception as ex:
        print(ex)
        print("enter Again...")
        continue
if emails:
    count = 0
    for email in emails:
        count +=1
        print("{}. email id:{}".format(count,email))
        storage.append(email)
    print("You have {} email id's".format(count))
    print("Do you want store the emails in a file or exit enter exit()/Y/N:")
    
    while True:
        option = input()
        if option =="Y" or "y":
            print("enter the path to store the file or leave it blank to store in deafult location:")
            path = input()
            while path:
                if path =="\n":
                    default = "email.txt"
                    os.system("touch email.txt")
                    f = open(default,'w')
                    f.write(str(storage))
                    f.close()
                    print("file saved as {}".format(deafult))
                    break
                else:
                    os.system(f"touch {path}")
                    f = open(path,'w')
                    f.write(str(storage))
                    f.close()
                    print("file saved in path:{}".format(path))
                    break
            break
        elif option == "N" or "n":
            break
        elif option == "exit()":
            print("Thank You...")
            break
        else:
            print("Enter the correct input again..")
            continue
else:
    print("No Emails found in the file.")
        
