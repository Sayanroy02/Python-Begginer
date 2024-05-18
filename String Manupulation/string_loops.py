sentence = "I love python"
a = len(sentence)  # len() to check length of string 
print(a)

# with while loop

i = 0  # initialize a value 
l = len(sentence)
while i < l:
    print(sentence[i] , end= " ")
    i += 1

print()
#unary minus operator

i= 1
l = len(sentence)
while i <=l:
    print(sentence[-i] , end = " ")  # using uninary minus (-i)
    i += 1

print()
#with for loop

for i in sentence:
    print(i,end= "")

#reverse a string 
print()

for i in sentence[ :  : -1]:
    print(i, end= " ")