#take a number from user then print multiplication table

num = int(input("Enter a number you want a table of : "))
times= int(input("How many times you want to multiply : "))
x = 1

while x <= times:
    print(f"{num} * {x} = {num * x}")
    x = x+ 1