"""
syntax: 
var_name ={key : Value , key2 : Value2}

operations in dictionary
add 
length
modify

"""
#Dictionary

#step 1 : initialise dictionary
menu = {} #empty dictionary

#step 2 : Add elements in dictionary
menu["Gulab Jamun"] = 40

#step 3: remove elements from dictionary
del menu["Gulab Jamun"] #use del keyword top delete element in dictionary

#how to access key 
menu["Palak Paneer"] = 20
menu["Butter Paneer"] = 40

price = menu["Gulab Jamun"]   # to access the key 

# update value 
menu["Butter Paneer"] = 120
price = menu["Butter Paneer"]
print(price)

# clear the dictionary
menu.clear  # to clean the dictionary

# to find length of a dictionary
print(len(menu)) # len function will find length of the dictionary 


print(menu)