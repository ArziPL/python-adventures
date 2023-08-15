# Day 10 - project 1

def calculation(number1, operator, number2):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        if number2 == 0:
            print("Can't divide by 0!")
            return number1 / 1
        return number1 / number2
    
number1 = int(input("Enter first number: "))
while True:
    operator = input("Enter operator (+-/*): ")
    number2 = int(input("Enter next number: "))
    current_answear = calculation(number1,operator,number2)
    print(f"Your answear: {current_answear}")
    another_operation = input("Do you want to continue with previosu answear? Type 'y' or 'n': ")
    if another_operation == 'n':
        exit()
    print("\n")
    print(f"Number 1: {current_answear}")
    number1 = current_answear
    