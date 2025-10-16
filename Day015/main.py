MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


profit = 0


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_update(used_resource):
    global resources, MENU

    if used_resource == "espresso":
        resources["water"] -= MENU[used_resource]["ingredients"]["water"]
        resources["coffee"] -= MENU[used_resource]["ingredients"]["coffee"]
    elif used_resource == "latte" or used_resource == "cappuccino":
        resources["water"] -= MENU[used_resource]["ingredients"]["water"]
        resources["coffee"] -= MENU[used_resource]["ingredients"]["coffee"]
        resources["milk"] -= MENU[used_resource]["ingredients"]["milk"]



def coin_processing(coffee_price):
    """Calculates the total amount of coins inserted by user"""
    global profit
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickel = int(input("How many nickel: "))
    penny = int(input("How many penny: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickel * 0.05) + (penny * 0.01)

    if total == MENU[coffee_price]["cost"]:
        print(f"Here is your {coffee_price}. Enjoy!!")

    else:
        if total < MENU[coffee_price]["cost"]:
            print(f"Sorry that is not enough money. Money refunded: ${total}")
        elif total > MENU[coffee_price]["cost"]:
            change = total - MENU[coffee_price]["cost"]
            total = MENU[coffee_price]["cost"]
            print(f"Here is your change: {round(change,2)}")
            print(f"Here is your {coffee_price}. Enjoy!!")
    profit += total

    print(profit)

    # print(total)



def resource_checker(resource):
    """Checks if there is sufficient resource to prepare the requested coffee"""
    if resource == "espresso":
        if MENU[resource]["ingredients"]["water"] <= resources["water"]:
            if MENU[resource]["ingredients"]["coffee"] <= resources["coffee"]:
                print("Order coming up!")
                coin_processing(resource)
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
    elif resource == "latte":
        if MENU[resource]["ingredients"]["water"] <= resources["water"]:
            if MENU[resource]["ingredients"]["coffee"] <= resources["coffee"]:
                if MENU[resource]["ingredients"]["milk"] <= resources["milk"]:
                    print("order coming up!")
                    coin_processing(resource)
                else:
                    print("Sorry there is not enough milk")
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water.")
    elif resource == "cappuccino":
        if MENU[resource]["ingredients"]["water"] <= resources["water"]:
            if MENU[resource]["ingredients"]["coffee"] <= resources["coffee"]:
                if MENU[resource]["ingredients"]["milk"] <= resources["milk"]:
                    print("order coming up!")
                    coin_processing(resource)
                else:
                    print("Sorry there is not enough milk")
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water.")
    resource_update(resource)






#TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

valid = True
while valid:
    order = input("What will you like? (espresso/latte/cappuccino): \n").lower()
    coffee = ["espresso", "latte", "cappuccino"]
    if order in coffee:
        print("Order processing...")
        resource_checker(order)
    elif order == "off":
        print("Shutting down ...")
        valid = False
    elif order == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${profit}")
    else:
        print("Invalid Input.")



# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# Done combined with first to do

# TODO: 3. Print Report.
# Done


# TODO: 4. Check resources sufficient?
#Done


# TODO: 5. Process coins.
#Done


# TODO: 6. Check Transaction Successful?
#Done



# TODO: 7. Make Coffee.
#Done and dusted buried




