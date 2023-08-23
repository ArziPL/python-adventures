from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    # Entry input
    action = input(f"\nType what you want to do ({menu.get_items()}report/off): ").lower()

    # Making any coffee
    if action in menu.get_items():
        coffee = menu.find_drink(action)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)

    # Report, refill if needed
    elif action == "report":
        coffee_maker.report()
        money_machine.report()
        refill_needed = input("Do you want to refill? Type 'y' or 'n': ")
        if refill_needed == "y":
            coffee_maker.refill()

    # Exit code
    elif action == "off":
        print("Goodbye!")
        exit()

    # Bad input
    else:
        print("Bad action, try again!")
