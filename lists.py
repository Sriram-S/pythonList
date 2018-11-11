from _collections import deque
lists=[]
lists.append("Hi")  #add objects to lists
print(lists)
print(lists.count("Hi"))   #count of the object present in the list
lists.extend([1,2,3])      #copy a list to another list
print(lists)    
print(lists[1]) 
lists.insert(0, "Hello")    #insert object at specified index
print(lists.__contains__("Hi"))  #boolean value to check if object is present in the list
print(lists)
print(lists.pop())    #delete last object from the lists
print(lists)
print(lists.pop(1))   #delete object from specified index from lists
print(lists)
print(lists.remove(1))  #remove the value from lists
print(lists)
print(lists.reverse())   #Reverse the lists value
print(lists)
lists.pop(1)
lists.extend([2,3,4,5,6])
# Sorting

lists.sort(reverse=True)  #sort in descending
print(lists)

stringlist=["Hi","Hello","Pythondev"]
stringlist.sort(key=len, reverse=True) #sorted using key len function - Sort based on total length of each strings in the list
print(stringlist)

#Iteration of lists
list_demo=["Hi",2,"3.0",'ddf',4]
for i in list_demo:
    if(isinstance(i, str)):
        print(i.upper())
    else:
        print(i)
        
for i in list_demo:
    if i=="Hi":
        print("Suceesfully found the value")
        
#Slicing
print(lists[1:]) # Print elements from index 1
print(lists[:3]) #print elements from index 0 to 2
print(lists[0:1]) #print element 0

#Copy lists
#Shallow copy
lists_duplicate=lists
print(lists_duplicate)
lists_duplicate.append("Added after shallow copy")
print(lists_duplicate)
print(lists) 
print(id(lists))  #returns value of the id which is referenced
print(id(lists_duplicate))  #returns value of the id which is referenced - both will have same value


#deep copy
import copy
lists_copied=copy.deepcopy(lists)
lists_copied.append(2)
print(lists_copied)
print(lists)
print(id(lists))
print(id(lists_copied))


#Using lists as queues
list=[1,2,3,4]
from collections import deque
queue=deque(list)
print(queue)
queue.popleft()
print(queue)


#Precise way to create lists of some operations
#Normal Way
listdemo=[]
for i in range(2,10,2):
     listdemo.append(i**2)
print(listdemo)     

#Method 2
listdemo_precise=[i**2 for i in range(2,10,2)]
print(listdemo_precise)
