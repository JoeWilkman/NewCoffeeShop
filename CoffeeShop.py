x = True

print("Welcome to Wire Village Coffee Shop.\n")

name = input("What is the name you would like to use for the order?\n")

if name == "Zak":
    print("Get out of here! All Zaks are evil!")
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
        whipped_cream = input("Would you like to add whipped cream on that for $2 more?\n")
        if whipped_cream == "Yes":
            price = 7
        else:
            price = 5
        break
    elif order == "You" or "I'd like to order you":
        print("That is completely inappropriate! I am going to have to ask you to stay still while I load the piece!")
        exit()
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
elif payment_method == "Credit Card" or "Debit Card":
    print("Alright, you can either use the chip or feel free to use the touch-to-pay option as well.")
elif payment_method == "Apple Pay":
    print("Okay, just tap your phone here. It may take a second or two.")
elif payment_method == "Venmo":
    print("Just scan the QR code here; we have a business account set up for all purchases in-shop now!")
elif payment_method == "Check":
    print("Wow... I uh... haven't seen someone use one of these yet. Let me just figure this out for you.")

print("We thank you so much for coming in today! If you would like to leave a tip, you can use either the tip jar or use the QR codes that each employee have in order to tip them via Venmo!")
