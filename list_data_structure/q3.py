"""
take list in input 
and then return maxium and minimum 
"""

def value():
    value_list = []
    user= int(input("how many numbers you want to put in list ? = "))
    for i in range(user):
        num = int(input(f"Enter number for {i} : "))
        value_list.append(num)
    print(value_list)
    maximum = max(value_list)  #using max function to ruturn maximum value
    minimum = min(value_list)  #using min function to ruturn minimum value
    print(f"Your maximum value in list is {maximum} \nand minimum value in list is {minimum}")

value()
