from art import logo2
import random

THE_NUMBER = random.randint(1,100)

def set_difficulty(difficulty):
    lives = 0
    if difficulty == "hard":
        lives = 5
        return lives
    else:
        lives = 10
        return lives

def game_over(lives_left):
    if lives_left == 0:
        print(f"Game over. You lose. The number was {THE_NUMBER}")
    else:
        print(f"The number was {THE_NUMBER}! You win!")


# ***************************Game starts here**************************
print(logo2)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
user_lives = set_difficulty(game_difficulty)

is_game_over = False
while(user_lives > 0) and (is_game_over != True):
    print(f"You have {user_lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess != THE_NUMBER:
        if user_guess > THE_NUMBER:
            user_lives -= 1
            print("Too high.")
            if user_lives > 0:
                print("Guess again.")
        else:
            user_lives -= 1
            print("Too low.")
            if user_lives > 0:
                print("Guess again.")
    else:
        is_game_over = True

game_over(user_lives)