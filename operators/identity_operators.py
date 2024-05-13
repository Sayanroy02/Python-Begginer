#IDENTITY OPERATORS 

#Used to compare memory location of two objects 

"""
Use two operators 
- is 
- is not
"""

#example 

list1= [1,2,3,4,5]
list2= [2,3,4,5,6]
list3=list1
print(list1 is list3)  # this means that items in list 1 is there in list 3? returns "true"
print(list1 is not list2)  # this means that items in list 1 is not there is list 2 ? - returns "True"