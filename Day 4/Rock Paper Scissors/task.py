import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Hands = [""]

Hands[0] = rock
Hands.append(paper)
Hands.append(scissors)

# Take user choice
User_Hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Make the Computer's choice random
Computer_Hand = random.randint(0, 2)

# Output hand user and computer hands
if User_Hand >= 0 and User_Hand < 3:
    print(Hands[User_Hand])
    print("Computer chose:")
    print(Hands[Computer_Hand])

# Check who won
if User_Hand == 0: # User chose Rock
    if Computer_Hand == 0:
        print("Draw")
    elif Computer_Hand == 1:
        print("You lose")
    else:
        print("You win")
elif User_Hand == 1: # User chose Paper
    if Computer_Hand == 0:
        print("You win")
    elif Computer_Hand == 1:
        print("Draw")
    else:
        print("You lose")
elif User_Hand == 2: # User chose Scissors
    if Computer_Hand == 0:
        print("You lose")
    elif Computer_Hand == 1:
        print("You win")
    else:
        print("Draw")
else:
    print("Invalid chose. You lose.")
