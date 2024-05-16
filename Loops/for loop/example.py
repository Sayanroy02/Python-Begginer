# Print numbers from 1 to 100 that is divisible by 3
for i in range(1, 101):
    if i % 3 == 0:
        print(i)


#take user input from user where user will search that what numbers r divisible by given number 

start_num = int(input("Enter start number = ")) 
end_num = int(input("Enter end number = "))

new_end_num = end_num + 1

divisor = int(input("Enter divisor : "))

for i in range(start_num , new_end_num):
    if i % divisor == 0:
        print(i)