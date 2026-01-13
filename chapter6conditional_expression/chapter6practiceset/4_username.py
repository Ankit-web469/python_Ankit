#length of username 
name=input("enter a name : ")
if(len(name)<10):
    print(f"its contain less than 10 char {len(name)}",name)
else:
    print(f"it contain more than 10 char {len(name)}",name)