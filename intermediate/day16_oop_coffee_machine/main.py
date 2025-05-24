from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


#---------- INITIALISE ----------#

menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()


#---------- INPUT HANDLERS ----------#

VALID_DRINKS = sorted(item.name for item in menu.menu)
VALID_COMMANDS = ["off", "report", "refill", "menu"]
VALID_INPUTS = VALID_DRINKS + VALID_COMMANDS

def get_choice(prompt):
    """Prompt user for drink choice or command, case-insensitive."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in VALID_INPUTS:
            return choice
        print(f"Invalid input. Please enter one of: {', '.join(VALID_INPUTS[:3])}.")


def get_number(prompt):
    """Prompt for a positive number, 0 is allowed"""
    while True: 
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Please enter a positive number.")
            elif not amount.is_integer():
                print("Please enter a whole number.")
            else:
                return int(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")


#---------- COFFEE MACHINE FUNCTIONS ----------#

def print_menu():
    """Display the drink options and prices"""
    print("Available drinks:")
    for item in menu.menu:
        print(f"- {item.name.title()}: {money.CURRENCY}{item.cost:.2f}")


def refill_resources():
    """Allow user to refill resources"""
    print("Refilling resources...")
    for item in coffee_machine.resources:
        unit = "ml" if item != "coffee" else "g"
        amount = get_number(f"How many {unit} of {item} would you like to add?: ")
        coffee_machine.resources[item] += amount
    print("Resources refilled.\n")


#---------- COFFEE MACHINE LOOP ----------#

def start_coffee_machine():
    """Main program loop"""
    machine_on = True

    while machine_on:
        choice = get_choice(f"\nWhat would you like? ({'/'.join(VALID_INPUTS[:3])}): ")
        if choice == "off":
            machine_on = False
        elif choice == "report":
            coffee_machine.report()
            # money.report()
            print(f"Money: {money.CURRENCY}{money.profit:.2f}")
        elif choice == "menu":
            # print(menu.get_items())
            print_menu()
        elif choice == "refill":
            refill_resources()
        else:
            drink = menu.find_drink(choice)
            if drink and coffee_machine.is_resource_sufficient(drink):
                process_transaction = money.make_payment(drink.cost)
                if process_transaction:
                    coffee_machine.make_coffee(drink)


#---------- ENTRY POINT ----------#

if __name__ == "__main__":
    start_coffee_machine()