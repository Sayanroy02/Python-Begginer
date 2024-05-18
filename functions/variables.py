"""
Local variables and Global variables

Variables that are defined inside a function and cannot use that variable outside a function is called local variables.
"""

#example of local variables

def into(a,b):
    a = 10
    b = 20
    c = a* b
    return c
x = into(10,30)  # will not print product of the attribute because local variable is already defining the a and b 
print(x)

#example of global variable

def mul(a,b):
    c = a *b
    return c
a= 44
b = 20
x = mul(a,b)
print(x)