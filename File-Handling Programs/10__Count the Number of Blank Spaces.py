file=input("Enter The  File Name with Extension For Open::")
count=0
with open(file,"r") as f:
    for line in f:
        words=line.split()
        for word in line:
            for letter in word:
                if(letter.isspace):
                    count=count+1
print("Number of Occurance Blank Spaces::",count)
