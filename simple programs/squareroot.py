"""
find square root of a number by taking user inputs
and print it Saying "Square root of $num is = $ root"
"""
#import sqrt(square root) module from math library 
from math import sqrt

# TAKE USER INPUT
num = float(input("Provide me a number to find the square root ="))

# FORMULAE 
root = sqrt(num)

# PRINT THE RESULT AND  use =>{} to use the variables as a print statement 
print (f"Square root of {num} is = {root}")

