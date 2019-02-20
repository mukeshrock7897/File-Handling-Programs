file1=input("Enter The 1st File Name with Extension For Open::")
file2=input("Enter The 2nd File Name with Extension For Open::")
with open(file1,"r") as f:
    with open(file2,"w") as f1:
        for line in f:
            f1.write(line)
