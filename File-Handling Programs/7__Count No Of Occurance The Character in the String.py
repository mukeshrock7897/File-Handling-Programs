file=input("Enter The File Name with Extension For Open::")
char=input("Enter The Occurance of letter::")
count=0
with open(file,'r') as f:
    for line in f:
        words=line.split()
        for i in words:
            for letter in i:
                if(letter==char):
                    count=count+1
print("The Number Of Occurance",count)
