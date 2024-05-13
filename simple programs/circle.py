"""
find a area of a circle , by taking radius from the user 
"""
# import constant pi from math module
from math import pi

#taking the radius as user input 
radius = float(input("enter radius of a circle ="))

# formulae to get area of a circle
area = pi * (radius ** 2)
#formulae to get perimeter of a circle
perimeter = 2 * pi * radius

#printing the result
print(f"tHE AREA OF A CIRCLE ACC. TO RADIUS  is {area}")
print(f'Perimeter of circle acc. to the radius is {perimeter}')