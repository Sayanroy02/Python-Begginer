"""Control statements are statements which control or change the flow of execution

Types of conditional /control statements 
1 - if
2 - if elif
3 - if elif else

4 - while loop
5 - for loop

6 - break statement
7 - continue statements 
8 - pass

9 - assert statements 
10 - return statements 

"""

#if statement 

if 2>1:
    print("Greater")


#example 1- take a user input and then check its even or odd(if else)

num = input("enter a number to check its even or odd :")
if int(num) % 2 == 0:                             #this is checking that  the number divided by 2 is giving remainder 0 or not  
    print("The number" , num ," is even")
else:
    print("The number" , num , "IS odd")


