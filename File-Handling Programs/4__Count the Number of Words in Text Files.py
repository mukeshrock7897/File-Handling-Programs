file=input("Enter The File Name with Extension::")
words=0
with open(file,'r') as f:
    for i in f:
        word=i.split()
        words=words+len(word)
    print("Total Number of Words::",words)
    
