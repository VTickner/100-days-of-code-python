from coffee_machine_menu import MENU

#---------- INITIALISE ----------#

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0.0

#---------- INPUT HANDLERS ----------#

VALID_DRINKS = ["cappuccino", "espresso", "latte"]
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

def print_report():
    """Display current resources and profit"""
    for item, amount in resources.items():
        unit = "ml" if item != "coffee" else "g"
        print(f"{item.title()}: {amount}{unit}")
    print(f"Money: ${profit:.2f}")


def print_menu():
    """Display the drink options and prices"""
    print("Available drinks:")
    for drink, price in MENU.items():
        print(f"- {drink.title()}: ${price['cost']:.2f}")


def is_resource_sufficient(ingredients):
    """Check if there are enough resources to make the drink"""
    for item, required in ingredients.items():
        if required > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def refill_resources():
    """Allow user to refill resources"""
    print("Refilling resources...")
    for item in resources:
        unit = "ml" if item != "coffee" else "g"
        amount = get_number(f"How many {unit} of {item} would you like to add?: ")
        resources[item] += amount
    print("Resources refilled.\n")


def collect_payment():
    """Prompt user to insert coins and return total in dollars."""
    print("Please insert coins.")
    total = get_number("How many quarters?: ") * 0.25
    total += get_number("How many dimes?: ") * 0.10
    total += get_number("How many nickels?: ") * 0.05
    total += get_number("How many pennies?: ") * 0.01
    return total


def process_transaction(payment, cost):
    """Update profit and return True if enough payment is received"""
    global profit
    if payment >= cost:
        change = payment - cost
        print(f"Here is ${change:.2f} in change.")
        profit += cost
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


def make_coffee(drink_name, ingredients):
    """Deduct ingredients from resources and serve the coffee"""
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name} ☕ Enjoy!\n")


#---------- COFFEE MACHINE LOOP ----------#

def start_coffee_machine():
    """Main program loop"""
    machine_on = True

    while machine_on:
        choice = get_choice("\nWhat would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            machine_on = False
        elif choice == "report":
            print_report()
        elif choice == "menu":
            print_menu()
        elif choice == "refill":
            refill_resources()
        else:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = collect_payment()
                if process_transaction(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])


#---------- ENTRY POINT ----------#

if __name__ == "__main__":
    start_coffee_machine()