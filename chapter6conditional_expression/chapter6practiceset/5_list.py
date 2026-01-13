#to check the name present in list or not 
l=["Ankit","ayush","harsh","anshul","akshay"]
name=input("enter a name to search: ")
if(name in l):
    ind=l.index(name)
    print("name found",ind)
else:
    print("not found")