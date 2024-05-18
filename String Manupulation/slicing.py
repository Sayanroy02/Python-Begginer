"""
slicing

string_name[start:stop:step]
if we dont write start , python will consider it a 0
if we dont write stop , python will consider it a n-1
if we dont write step , python will consider it a +1
"""


string = "I love Python"

for i in string[2 : 13 : 2]:
    print(i , end=" ")