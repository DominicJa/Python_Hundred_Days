# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)

bidders = {}

user = input("What is your name?: ")
bid = int(input("What's your bid?: $"))

bidders[user] = bid

more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
while more_bidders == "yes":
    print("\n" * 20)
    print(logo)
    user = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[user] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

highest_bid = -1
winner = ""

for key in bidders:
    if highest_bid < bidders[key]:
        highest_bid = bidders[key]
        winner = key

print("\n" * 20)
print(logo)
print(f"The winner is {winner} with a bid of ${bidders[winner]}.")