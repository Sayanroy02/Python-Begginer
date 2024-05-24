"""
def a function where user will enter how many number he wants to put and then take all those numbers 

"""

def sum():
    lst =[]
    user = int(input("how many numbers you want to add ? = "))
    for i in range(user):
        choice = int(input(f"Enter element {i} = "))
        lst.append(choice)

    total = 0
    for i in range(len(lst)):
        total = total + lst[i]
    return f"total is {total}"

s =sum()
print(s)