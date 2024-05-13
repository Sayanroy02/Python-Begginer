"""
Use of input finction
1- to take input form user
2- Returns a datatype - string

SYNTAX
name = input("Helloo : ")
"""
#example to take input from user
ask = input("What do you want ? (Tea / Coffee) :")
print("I want" , ask)


#example of the return datatype of input 
num1 = input("Enter Number :")
num2 = input("Enter Number :")

num3 = num1 + num2 #its in string 

print (num3 ,type(num3)) # this will retuen string datatype 

#to change the datatype from string to integer
num3 = int(num1) + int(num2)
print(num3 , type(num3))  # this will return integer datatype 
