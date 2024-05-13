"""
String is a text in python wrote inside ""(double quotation)
"""
# create a string 
name = "Sayan"

# concatinate string
surname = "Roy"
print(name,"" + surname)  # added , "" to give a gap between two strings 

#access a charecter 
language = "Python"
first_char = language[0]  #to access charecter by passing index 
third_char = language[3]
print(first_char ,"" + third_char)

#How to replace a string 
sentence  = "I love C programming"
new_sentence = sentence.replace("C","Python")  #to replace a sentence use variable name then use replace function and pass what you want to replace with what seperating them with commas 
print(sentence)
print(new_sentence)

#find length of a string 
srg = "I love Python"
print(len(srg))  #use len function to find length of a variable 


#convert int to string
name = "Sayan"
age = 21
print(name, "" + str(age))
