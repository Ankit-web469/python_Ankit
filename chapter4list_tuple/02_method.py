l1=[2,1,4,3,5,6]
print(l1)
#sort()-arrange data in ascending order
l1.sort(reverse=True)
print(l1)
#reverse()-arrange data in descending order
l1.reverse()
print(l1)
#append()-add the new element at the end 
l1.append("pathak")
print(l1)
#insert-this will value at givem index eg:(insert(2,5))
l1.insert(3,8) #insert 8 at index 3  
print(l1)
#pop-will delete value at given index 
l1.pop(3)
print(l1)
#remove-it will delete  the given value
l1.remove("pathak")
print(l1) 
l1.extend([12,18])
print(l1)
l=sum(l1)  
print(l)
m=max(l1)
print(m)
l1.clear()
print(l1)