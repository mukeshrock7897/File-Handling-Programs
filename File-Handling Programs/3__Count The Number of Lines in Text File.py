file=input("Enter The File Name with Extension::")
line=0
with open(file,'r') as f:
    for i in f:
        line=line+1
    print("Total Number of Lines::",line)
    
