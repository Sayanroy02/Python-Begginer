"""
MEMBERSHIP OPERATOR

two methods 
 in -> output : true/false
 not in
"""

main_str= input("Enter main string = ")
sub_str = input("Enter sub string = ")

if sub_str in main_str:
    print(f" ${sub_str} is found in ${main_str}")
else:
    print(f" ${sub_str} is not found in ${main_str}")