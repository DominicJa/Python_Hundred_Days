import art
import random
import game_data

def pick_game_data():
    """Returns a random person/place from game_data's list of dictionaries"""
    random_element = random.choice(game_data.data)
    return random_element

def display_compare(compare1, compare2):
    print(f"Compare A: {compare1['name']}, a {compare1['description']}, from {compare1['country']}")
    print(art.vs)
    print(f"Against B: {compare2['name']}, a {compare2['description']}, from {compare2['country']}")

def next_round(compare1, compare2):
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == "a":
        if compare1['follower_count'] >= compare2['follower_count']:
            return True
        else:
            return False
    elif guess == "b":
        if compare2['follower_count'] >= compare1['follower_count']:
            return True
        else:
            return False
    else:
        return False

def game_over(final_score):
    print("\n" * 5)
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {final_score}")



# Game Starts Here
score = 0
print(art.logo)
compare_a = pick_game_data()
compare_b = pick_game_data()

while compare_a == compare_b:
    compare_b = pick_game_data()

display_compare(compare_a, compare_b)

continue_ = next_round(compare_a, compare_b)
while continue_:
    print("\n" * 5)
    print(art.logo)
    score += 1
    print(f"You're right! Current score: {score}")

    compare_a = compare_b
    compare_b = pick_game_data()

    while compare_a == compare_b:
        compare_b = pick_game_data()

    display_compare(compare_a, compare_b)

    continue_ = next_round(compare_a, compare_b)

game_over(final_score=score)