"""
1- append
2 - update
3 - delete
"""

#append

a = [1,2,3,4,5]
a.append("Sayan") # append to add a element into a list , but it will add the value in end
print(a)

#update 
a1 = ["sayan" , 20 , "M" , "English"]
a1[0] = "Sayan Roy"  # to update an element in any index number 
print(a1)

#delete 
a2 = ["sayan" , 20 , "M" , "English"]
del a2[1]
print(a2)
