file=input("Enter The File Name With Extension::")
with open(file,'r')as f:
    print("The Contents are Availble In This Files Are::\n")
    print(f.read())
    
