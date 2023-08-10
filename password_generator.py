# Day 5 - project 2
import string
import random

# User input + tests
pass_len = int(input("How many letters would you like in your password? "))
pass_symbols = int(input(f"How many symbols would you like? Maximum available: {pass_len} => "))
while pass_symbols > pass_len:
    pass_symbols = int(input(f"Please, write the correct number for amount of symbols. Maximum available: {pass_len} => "))
pass_numbers = int(input(f"How many numbers would you like? Maximum available: {pass_len - pass_symbols} => "))
while pass_numbers > pass_len - pass_symbols:
    pass_numbers = int(input(f"Please, write the correct number for amount of numbers. Maximum available: {pass_len - pass_symbols} => "))

# Generating random char password
password = [None] * (pass_len)
for i in range(1,pass_len + 1):
    password[i - 1] = random.choice(string.ascii_letters)

# Adding random symbols and numbers
while pass_symbols > 0 or pass_numbers > 0:
    current_position = random.randint(0,pass_len - 1)
    if(password[current_position] in string.ascii_letters):
        if pass_symbols > 0:
            password[current_position] = random.choice(string.punctuation)
            pass_symbols = pass_symbols - 1
        else:
            password[current_position] = random.choice(string.digits)
            pass_numbers = pass_numbers - 1

print(f"Your password is {''.join(password)}") 


# Easier way from tutorial, you need to comment out first way :\
# password = []
# for i in range(pass_len - pass_symbols - pass_numbers):
#     password.append(random.choice(string.ascii_letters))

# for i in range(pass_symbols):
#     password.append(random.choice(string.punctuation))

# for i in range(pass_numbers):
#     password.append(random.choice(string.digits))

# random.shuffle(password)
# print(f"Your password is {''.join(password)}") 
