import os
file=input("Enter The File Name With Extension::")
if os.path.isfile(file):
    with open(file,'r')as f:
        print("The Contents are Availble In This Files Are::\n")
        print(f.read())
else:
    print("File Does Not Exist ")
