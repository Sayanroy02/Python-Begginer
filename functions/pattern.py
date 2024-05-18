def triangle():
    lines = int(input("Enter number of lines = "))
    for i in range(1, lines + 1):
        for j in range(i):
            print("*" , end = " ")
        print()
    return lines

triangle_shape=  triangle()
print(triangle_shape)