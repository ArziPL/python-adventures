from ingredients import *

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}


def making_coffee(coffee, resources_dict):
    # Checking resources
    resources_list = list(resources.values())
    coffee_ingredients = list(MENU[coffee]["ingredients"].values())
    for index, ingredient in enumerate(coffee_ingredients):
        if resources_list[index] < ingredient:
            print("There are not enough ingredients, report the problem to the staff!")
            return False

    # Coin logic, insert, check if enough then decrease resource
    coin_result = handling_coins(coffee, MENU[coffee]['cost'])
    if coin_result:
        handling_resources(coffee, resources_dict)


def handling_coins(coffee, coffee_price):
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
    resources_dict["water"] -= MENU[coffee]["ingredients"]["water"]
    resources_dict["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources_dict["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    resources_dict["profit"] += MENU[coffee]["cost"]


def report(resources_dict, action="print"):
    """Printing resources, if action fill then filling them up with notification"""
    if action == "fill":
        print("Stocks replenished!")
        resources_dict["water"] += 300
        resources_dict["milk"] += 200
        resources_dict["coffee"] += 100
    print("Your report:")
    print(f"Water: {resources_dict['water']}ml")
    print(f"Milk: {resources_dict['milk']}ml")
    print(f"Coffee: {resources_dict['coffee']}g")
    print(f"Profit: {resources_dict['profit']}PLN")


# Main
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
        making_coffee("espresso", resources)
    elif user_choice == 2:
        making_coffee("latte", resources)
    elif user_choice == 3:
        making_coffee("cappuccino", resources)
    elif user_choice == 4:
        report(resources)
    elif user_choice == 5:
        report(resources, "fill")
    elif user_choice == 6:
        print("Goodbye!")
        exit()
