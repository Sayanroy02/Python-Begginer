num1 = int(input("Enter a start number = "))
num2 = int(input("Enter a end number = "))

x = num2 + 1  # adding 1 to num2 as stop number will be excluded
for i in range(num1 , x , -1):
    print(i)