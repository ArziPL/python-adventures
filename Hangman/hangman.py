# Day 7 - project 1
import hangman_art
import words
import random
import os

# Base functions


def clear(): return os.system('cls')  # to clear command console


# Base variables
guess_string = random.choice(words.list_of_words)
guess_word = list(guess_string.strip())  # formatting guess word
stage_of_hangman = 6  # lifes
currently_guessed = ["_"] * len(guess_word)  # list of all good guesses
already_guessed_letters = []  # list of already guessed letters

# Intro
print("Welcom to hangman!")
print(hangman_art.logo)
input("Ready to start a game? Click enter to start!")
clear()

# Game itself
while True:
    # Basic logic
    print(f"Currently guessed: {currently_guessed}")
    print(hangman_art.stages[stage_of_hangman])
    current_char = input("Make a guess:")

    # Making sure no more then one symbol is written
    while (len(current_char) != 1):
        current_char = input("One symbol only, please: ").lower()

    # Bad guess option -> end of game/bad guess/already guessed letter
    if current_char not in guess_word or current_char in already_guessed_letters:
        stage_of_hangman -= 1

        # Lost game moment
        if stage_of_hangman == 0:
            clear()
            print(hangman_art.stages[stage_of_hangman])
            print("You lost!")
            break
        clear()

        # Bad word guessed
        if current_char not in guess_word:
            print("Bad letter")
            continue

        # Already guessed word
        else:
            print("Already guessed!")
            continue

    # Good guess option -> if char match guess_word at index x, put at the same index same letter to currently_guessed and add it to already_guessed_letters
    for index, letter in enumerate(guess_word):
        if current_char == letter:
            currently_guessed[index] = current_char
            clear()
            print("Good job! Next one")
            already_guessed_letters.append(current_char)

    # Checking final win condition - if currently_guessed == guess_word win (after putting new letters to word/after checking lost condition)
    if currently_guessed == guess_word:
        clear()
        print(f"Guess word: {''.join(guess_word)}")
        print(hangman_art.stages[stage_of_hangman])
        print("You saved him! Great job!")
        break
