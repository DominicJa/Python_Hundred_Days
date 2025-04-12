from art import logo
import random


# Deck of cards
playing_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# **************Functions******************************
# TODO: Make pick_card function check if 11 (Ace) will make the player/dealers score go over 21 if so make it 1.
def calculate_score(list_):
    """This function takes a list (player or dealer) and calculates all the 'cards' in it"""
    card_total = 0
    for card in list_:
        card_total += card
    return card_total

def pick_card(list_):
    """This function takes a list (player or dealer) and puts a card from the main list into it."""
    score = calculate_score(list_)
    random_card = random.choice(playing_cards)
    if random_card != 11:
        list_.append(random_card)
    else:
        if (score + 11) <= 21:
            list_.append(random_card)
        else:
            list_.append(1)

def display_player(list_, score):
    print(f"Your cards: {list_}, current score: {score}")

# **************************Game Start Here************************************
keep_playing = input("Do you want to play a game of Blackjack Type 'y' or 'n': ").lower()

while keep_playing == "y":
    print(logo)

    #Put at the beginning to reset run
    player_cards = []
    dealer_cards = []

    # Get the player's first two cards and print their score
    pick_card(player_cards)
    pick_card(player_cards)
    players_score = calculate_score(player_cards)
    display_player(player_cards, players_score)

    # Start calculating computer's first card and show it
    pick_card(dealer_cards)
    dealers_score = calculate_score(dealer_cards)
    print(f"Computer's first card: {dealers_score}")

    # Ask player if they want to hit.
    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while (another_card == "y") and (players_score <= 21):
        pick_card(player_cards)
        players_score = calculate_score(player_cards)
        display_player(player_cards, players_score)

        print(f"Computer's first card: {dealers_score}")

        if players_score >= 21:
            another_card = "n"
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    # Make dealer pick second card and more if needed (if dealers_score < 17 after second card pick another)
    if players_score <= 21:
        while (dealers_score < 17) and (not(dealers_score > players_score)):
            pick_card(dealer_cards)
            dealers_score = calculate_score(dealer_cards)

    # Show the player's and dealer's final hands
    print(f"Your final hand: {player_cards}, final score: {players_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealers_score}")

    # Determine the results of the game
    if players_score > 21:
        print("You went over. You lose")
    elif dealers_score > 21:
        print("Dealer went over. You win")
    elif players_score < dealers_score:
        print("Dealer wins.")
    elif players_score > dealers_score:
        print("You win.")
    else:
        print("Draw.")

    # Does the play want to keep playing?
    keep_playing = input("Do you want to play a game of Blackjack Type 'y' or 'n'").lower()