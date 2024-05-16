"""
A order management system where customer will choose what to order after ordering a question will be asked that 
do you want to order anything ? If yes then again show the menu and customer wil, 
place order again and the bill with amount will be printed
"""

# create a dictionary (menu)
menu  = {
    "Pizza" : 40,
    "Pasta" : 80,
    "momo"  : 40,
    "Veg-Chowmin":35,
    "Egg-Chowmin":45,
    "Chicken-Chowmin":60,
    "Tea" : 10,
    "Coffee" : 10,
    "Veg Thali" : 100,
    "Non-veg Thali" : 300,
}
# greet customer !
print("Welcome to Sanju Da Dhabba !")

#show menu 
print("Here's our menu:\nPizza: Rs 40\nPasta : Rs 80\nMomo : Rs 40\nVeg-Chowmin :Rs 35\nEgg Chowmin : Rs 45\nChicken-Chowmin : Rs 60\nTea : Rs 10\nCoffee : Rs 10\nVeg Thali : Rs 100\nNon-Veg Thali : 300")

total_order=0  #this variable will store the total value

item1= input("What do you want to order ?")
if item1 in menu:
    total_order += menu[item1]
    print(f"Your item {item1} has been added to your order")
else:
    print(f"Your order of {item1} is not available yet !")

another_order = input("Do you want to order anything else ?(Yes / No)")
if another_order == "Yes":
    item2 =input("Enter the name of item you want to order : ")
    if item2 in menu:
        total_order += menu[item2]
        print(f"Your order of {item2} has been placed")
    else:
        print(f"Your order of {item2} is not available")
    
print(f"Thank you for ordering. You total payable amount is {total_order}")




