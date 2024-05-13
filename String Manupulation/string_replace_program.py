#REPLACE MEDTHOD
"""
syntax

string.replace(old,value)
1- search the string
2- replace the string 
3- result 

Aim
1- take user input 
2- let user decide that does he wants to change the sentence or not
3- if yes , then thake user inputs of what he wants to change with which word 
4 - Print the new sentence  
"""

#string manupulation using user inputs

sentence = input("Enter a sentence : ") # taking a sentence
print("Your Sentence" ,sentence)
change = input("Do you want to change the sentence? (T/F)" ) # taking user decision

# use if else statement to manupulate user decision 
if change.upper() == "T" :
   word_to_replace = input("Word you want to replace:")  # Taking the word that user want to replace 
   word_to_use =input("Word you will used instead :")    # Taking the word  that user wants to replace with  
   new_sentence = sentence.replace(word_to_replace,word_to_use)  # using replace function and passing both the variables of replace and replace with 
   print("Edited sentence = " , new_sentence)
else: 
 print(sentence)

