# Day 12 - project 1
import random

# Main game logic to repeat


def game():
    # Game variables
    lives = 0
    guess_num = random.randint(1, 100)
    guessed_num = None
    difficulty = input("Choose your difficulty, type 'easy' or 'hard': ")
    if difficulty == "easy":
        print('Your have 10 attempts')
        lives = 10
    elif difficulty == "hard":
        print("You have 5 attempts")
        lives = 5

    # Game itself
    while True:
        guessed_num = int(input("Guess number: "))
        # If correct
        if guessed_num == guess_num:
            print(
                f"Congratulations! You won :) Number to guess was {guess_num}")
            return
        # If no more lives
        elif lives == 1:
            print(f"Bad! You lost, number to guess was {guess_num}")
            return
        # If bad guess with lives
        else:
            if guessed_num > guess_num:
                lives -= 1
                print(f"Bad! It's lower, remaining lives: {lives}")
            else:
                lives -= 1
                print(f"Bad! It's higher, remaining lives {lives}")


print("Welcom to the higher-lower game!")
while True:
    game()
    # Ask if user want to play another game
    another_game = input("Do you want to play another one? Type 'y' or 'n'")
    if another_game == "y":
        continue
    else:
        print("Thanks for playing :)")
        break
