#to check spam comment 
p1="Make a lot of money"
p2="buy now"
p3="subscribe now"
p4="ckick this"
m=input("enter a comment:")
if((p1 in m) or (p2 in m) or (p3 in m) or (p4 in m) ):
    print("this is a spam")

else:
    print("no spam ")
