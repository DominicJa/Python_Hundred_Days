from random import choice

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
Choice = input("You're at a cross road. Where do you want to go?\n\tType \"left\" or \"right\"\n")
Choice = Choice.lower()
if Choice == "left":
    Choice = input("You reach a beach shore. There two things that catch your eye. The first is a boat and the second "
                   "is an island in swimming distance. Where do you want to go?\n\tType \"boat\" or \"island\"\n")
    Choice = Choice.lower()
    if Choice == "boat":
        Choice = input("You get onto the boat and walk below deck. Down there you find three colored doors. Red, Yellow, "
                       "and Blue. Which door do you pick?\n\tType \"red\", \"yellow\", or \"blue\"\n")
        Choice = Choice.lower()
        if Choice == "red":
            print("You step into the red door and are turned into ash by the insane heat. Game Over")
        elif Choice == "yellow":
            print("You find the treason you have been looking for! You win!")
        elif Choice == "blue":
            print("You open the blue door. Before you even step inside you are pulled in by a creature and are eaten. Game Over.")
        else:
            print("Invalid option")
    elif Choice == "island":
        print("You attempt to swim to the island but are pulled down by an unknown force. You are never heard from again. Game Over")
    else:
        print("Invalid option")
elif Choice == "right":
    print("You get hit by a car! Game over")

else:
    print("Invalid option")