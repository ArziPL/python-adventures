# Day 7 - project 1
import hangman_art
import words
import random
import os

# Base variables
clear = lambda: os.system('cls')
guess_string = words.list_of_words[random.randint(0,8)]
guess_word = list(guess_string.strip())


print("Welcom to hangman!")
print(hangman_art.logo)
input("Ready to start a game? Click enter to start!")
clear()

stage_of_hangman = 6
currently_guessed = ["_"] * len(guess_word)
already_guessed = []
while True:
    print(f"Currently guessed: {currently_guessed}")
    print(hangman_art.stages[stage_of_hangman])
    current_char = input("Make a guess:")
    while(len(current_char) != 1):
        current_char = input("One symbol only, please: ").lower()
    
    if current_char not in guess_word or current_char in already_guessed:
        stage_of_hangman -= 1
        if stage_of_hangman == 0:
            clear()
            print(hangman_art.stages[stage_of_hangman])
            print("You lost!")
            break
        clear()
        if current_char not in guess_word:
            print("Bad letter")
            continue
        else:
            print("Already guessed!")
            continue

    for index,letter in enumerate(guess_word):
        if current_char == letter:
            currently_guessed[index] = current_char
            clear()
            print("Good job! Next one")
            already_guessed.append(current_char)
    if currently_guessed == guess_word:
        clear()
        print(f"Guess word: {''.join(guess_word)}")
        print(hangman_art.stages[stage_of_hangman])
        print("You saved him! Great job!")
        break
    



    


