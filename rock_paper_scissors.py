# Day 3 - project 1
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

signs = [rock, paper, scissors]

player_choice = signs[int(input("Enter 1 for rock, 2 for paper, 3 for scissors :) ")) - 1]
computer_choice = signs[random.randint(0,2)]

print(f"You choose:\n{player_choice}")
print(f"Computer choose:\n{computer_choice}")

if(player_choice == computer_choice):
    print("It's a draw!")
elif player_choice == rock and computer_choice == paper:
    print("You lose!")
elif player_choice == paper and computer_choice == scissors:
    print("You lose!")
elif player_choice == scissors and computer_choice == rock:
    print("You lose!")
else:
    print("You won!")