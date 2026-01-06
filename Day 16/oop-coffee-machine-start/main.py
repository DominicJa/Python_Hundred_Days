from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# A list of classes for the program to use
Menu_ = Menu()
CoffeeMaker_ = CoffeeMaker()
MoneyMachine_ = MoneyMachine()

# Start of main program
continue_ = True
while continue_:
    item = input(f"What would you like? ({Menu_.get_items()}):").lower()

    if item == "off":
        continue_ = False
    elif item == "report":
        CoffeeMaker_.report()
        MoneyMachine_.report()
    else:
        User_Item = Menu_.find_drink(item)
        if User_Item is not None:
            if CoffeeMaker_.is_resource_sufficient(User_Item):
                if MoneyMachine_.make_payment(User_Item.cost):
                    CoffeeMaker_.make_coffee(User_Item)

