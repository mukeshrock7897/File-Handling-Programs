file=input("Enter The  File Name with Extension For Open::")
with open(file,"r") as f:
    for line in f:
        words=line.split()
        for word in words:
            for letter in word:
                if(letter.isdigit()):
                    print(letter)
      
