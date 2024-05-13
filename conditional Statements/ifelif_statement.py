#IF ELIF STATEMENT

shopping_amt=int(input("Enter your total shopping amount = "))

if shopping_amt >= 10000:
    print("Yor are eligible for discount !")
elif shopping_amt >= 1 and shopping_amt <= 9999:  #use of elif to check another condition -
    print("You are not elegible for discounts. ")
else: 
    print("Re enter right amount")

