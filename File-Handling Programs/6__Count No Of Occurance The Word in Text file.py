file=input("Enter The File Name with Extension For Open::")
word=input("Enter The Occurance of Word::")
count=0
with open(file,'r') as f:
    for line in f:
        words=line.split()
        for i in words:
            if(i==word):
                count=count+1
print("The Number Of Occurance",count)
