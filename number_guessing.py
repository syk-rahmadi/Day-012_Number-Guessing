from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to set difficulty.
def turns():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#Function to run the game.
def game():
    print (logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    computer_answer = randint(1, 100)
    difficulty = turns()

    #Repeat the guessing functionality if they get it wrong.
    player_guess = 0
    while player_guess != computer_answer:
        print(f"You have {difficulty} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        difficulty = check_answer(player_guess, computer_answer, difficulty)
        if difficulty == 0:
            print("You've run out of guesses, you lose.")
            print(f"The number was, {computer_answer}.")
            return
        elif player_guess != computer_answer:
            print("Guess again.")

game()

