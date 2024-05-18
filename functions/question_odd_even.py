def check_odd_even():
    num = int(input("Enter a number to check if it is odd or even = "))
    if num % 2 == 0:
        print(f"The number ${num} is even")
    else:
        print(f"The number ${num} is odd")
    return num

user = check_odd_even()
print(user)
      