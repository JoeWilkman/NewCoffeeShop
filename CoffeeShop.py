x = True

print("Welcome to Wire Village Coffee Shop.\n")

name = input("What is the name you would like to use for the order?\n")

if name == "Zak":
    print("Get out of here Ben! All Zak's are evil!")
    exit()
else:
    print("Thank you " + name + " for coming in today.")

print("What would you like to order today?\n")

#order = input("Here is what we are currently serving: Black Coffee, Espresso, Iced Tea, Hot Tea, Hot Chocolate.\n")

#print("Here is what we are currently serving: Black Coffee, Espresso, Iced Tea, Hot Tea, Hot Chocolate.\n")
while x == True:
    order = input("Here is what we are currently serving: Black Coffee, Espresso, Iced Tea, Hot Tea, Hot Chocolate.\n")
    if order == "Black Coffee":
        price = 3
        break
    elif order == "Espresso":
        price = 5
        break
    elif order == "Iced Tea":
        price = 3
        break
    elif order == "Hot Tea":
        price = 3
        break
    elif order == "Hot Chocolate":
        price = 5
        break
    else:
        answer = input("I am really sorry, but we do not serve that item at this location. Can I interest you in something else?\n")
        if answer == "Yes":
            continue
        elif answer == "No":
            print("Thank you for coming in. We hope to see you soon!")
            exit()

quantity = input("How many " + order + "s would you like to order?\n")

total = price * int(quantity)

print("Thank you so much for your order!\n")
print("Your total today for the order will be: $" + str(total))

payment_method = input("How would you like to pay today?\n")

if payment_method == "Cash":
    print("Thank you so much. I will have your change in a moment!")