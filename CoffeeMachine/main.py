from ingredients import *

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}


def making_coffee(coffee):
    """Check if there's enough ingredients, ask for coins, return true if making coffee was hasssle free  """
    water_requirements = MENU[coffee]["ingredients"]["water"] > resources["water"]
    milk_requirements = MENU[coffee]["ingredients"]["milk"] > resources["milk"]
    coffee_requirements = MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]
    if water_requirements or milk_requirements or coffee_requirements:
        print("There are not enough ingredients, report the problem to the staff!")
        return False
    else:
        coin_result = handling_coins(coffee, MENU[coffee]["cost"])
        if coin_result:
            return True
        return False


def handling_coins(coffee, coffee_price):
    """Ask user for coins, check if there was enough then give away coffe with change"""
    print(f"Please, insert coins, it will be {MENU[coffee]['cost']}PLN")
    five_pln = int(input("Throw 5PLN: ")) * 5
    two_pln = int(input("Throw 2PLN: ")) * 2
    one_pln = int(input("Throw 1PLN: ")) * 1
    sum_of_coins = five_pln + two_pln + one_pln
    if sum_of_coins < coffee_price:
        print("You didn't put in enough money")
        return False
    else:
        print(f"Here's your {coffee}! Your change: {sum_of_coins - coffee_price}PLN")
        return True


def handling_resources(coffee, resources_dict):
    """Changing resources dict when coffee is made (- ingredients,+ profit)"""
    resources_dict["water"] -= MENU[coffee]["ingredients"]["water"]
    resources_dict["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources_dict["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    resources_dict["profit"] += MENU[coffee]["cost"]


def print_report(resources_dict):
    """Printing resources dict in pretty way"""
    print("Your report:")
    print(f"Water: {resources_dict['water']}ml")
    print(f"Milk: {resources_dict['milk']}ml")
    print(f"Coffee: {resources_dict['coffee']}g")
    print(f"Profit: {resources_dict['profit']}PLN")


def refill(resources_dict):
    """Adding ingredients to resources_dict (300 water, 200 milk, 100 coffee) and printing report on screen"""
    print("Stocks replenished!")
    resources_dict["water"] += 300
    resources_dict["milk"] += 200
    resources_dict["coffee"] += 100
    print_report(resources_dict)


# Simple thing, asking user for action in loop, then executing functions for those actions
while True:
    print("\n")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    print("4. Report")
    print("5. Refill")
    print("6. Off")
    user_choice = int(input("What would you like to do? Type number: "))
    if user_choice == 1:
        coffee_result = making_coffee("espresso")
        if coffee_result:
            handling_resources("espresso", resources)
    elif user_choice == 2:
        coffee_result = making_coffee("latte")
        if coffee_result:
            handling_resources("latte", resources)
    elif user_choice == 3:
        coffee_result = making_coffee("cappuccino")
        if coffee_result:
            handling_resources("cappuccino", resources)
    elif user_choice == 4:
        print_report(resources)
    elif user_choice == 5:
        refill(resources)
    elif user_choice == 6:
        print("Goodbye!")
        exit()
