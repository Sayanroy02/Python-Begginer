"""
Create a Python program that prompts the user to enter their age in years using the input function.
Convert this age from a string to an integer and store it in a variable. 
Then, calculate and print the age in months (assume 12 months in a year). 
For example, if the user enters "20", the program should output "You are 240 months old."
"""

age = input("Enter your Age = ")  #taking user input 
age_of_user = int(age) # changing datatype from string to integer 

#calculating the age in months (assume 12 months in a year).
age_in_months = age_of_user * 12

#printing the age in months
print(f"You are  {age_in_months}" + " months old " + f", according to your age {age}") 
