file=input("Enter The  File Name with Extension For Open::")
with open(file,"r") as f:
    for line in f:
        l=line.title()
        print(l)
