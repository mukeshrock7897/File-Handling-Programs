file1=input("Enter The File Name with Extension::")
with open(file1,'a') as f:
    write=input("Enter The Strings For Appending::\n")
    f.write(write)
print("Writing Completed ")

file2=input("Enter The File Name with Extension For Open::")
with open(file2,'r') as f:
    print("After Writing The Content Availble The Updated Contents")
    print(f.read())
    
