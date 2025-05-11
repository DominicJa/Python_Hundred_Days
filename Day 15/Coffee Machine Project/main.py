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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")

def resources_sufficient(drink):
    for key in MENU[drink]["ingredients"]:
        if resources[key] < MENU[drink]["ingredients"][key]:
            print(f"Sorry there is not enough {key}.")
            return False

    return True

def process_coins(drink):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    monetary_value = float((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))

    if monetary_value < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = monetary_value - MENU[drink]["cost"]
        change = round(change, 2)
        print(f"Here is ${change} in change.")
        resources["money"] += MENU[drink]["cost"]
        return True

def make_coffee(drink):
    for key in MENU[drink]["ingredients"]:
        resources[key] -= MENU[drink]["ingredients"][key]

    print(f"Here is your {drink}. Enjoy!")


# **************************Main project starts here*******************************************
Continue_ = True

while Continue_:
    user_drink = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_drink == "report":
        print_report()
    elif user_drink == "off":
        Continue_ = False
    elif user_drink == "espresso" or user_drink == "latte" or user_drink == "cappuccino":
        sufficient = resources_sufficient(user_drink)
        if sufficient:
            make_drink = process_coins(user_drink)
            if make_drink:
                make_coffee(user_drink)
    else:
        print("Invalid drink entered.")
