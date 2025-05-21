from coffee_machine_menu import MENU

#---------- INITIALISE ----------#

valid_inputs = ["cappuccino", "espresso", "latte", "off", "report"]
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

#---------- INPUT HANDLERS ----------#

def get_choice(prompt):
    """Prompt for either: 'espresso', 'latte' or 'cappuccino', hidden keywords 'off' or 'report', case-insensitive."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_inputs:
            return choice
        print(f"Invalid input. Please enter either '{valid_inputs[0]}', '{valid_inputs[1]}' or '{valid_inputs[1]}'.")


def get_number(prompt):
    """Prompt for a number"""
    while True: 
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


#---------- DATA HANDLERS ----------#

def get_report():
    """Print resources and profit"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")


def get_payment(drink):
    """Get payment and check there is enough money to purchase drink"""
    global profit

    print("Please insert coins.")
    quarters = get_number("How many quarters?: ")
    dimes = get_number("How many dimes?: ")
    nickles = get_number("How many nickles?: ")
    pennies = get_number("How many pennies?: ")
    money_inserted = ((quarters * 25) + (dimes * 10) + (nickles * 5) + pennies) / 100

    if money_inserted >= MENU[drink]["cost"]:
        change = money_inserted - MENU[drink]["cost"]
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {drink} ☕ Enjoy!")
        profit += MENU[drink]["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def check_resources(drink):
    """Check there is enough resources to make drink"""
    if drink == "espresso":
        water_remaining = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        milk_remaining = resources["milk"]
        coffee_remaining = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
    elif drink == "latte":
        water_remaining = resources["water"] - MENU["latte"]["ingredients"]["water"]
        milk_remaining = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        coffee_remaining = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
    elif drink == "cappuccino":
        water_remaining = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        milk_remaining = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        coffee_remaining = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]

    if water_remaining >= 0 and milk_remaining >= 0 and coffee_remaining >= 0:
        paid = get_payment(drink)
        if paid == True:
            resources["water"] = water_remaining
            resources["milk"] = milk_remaining
            resources["coffee"] = coffee_remaining
    elif water_remaining < 0:
        print("Sorry there is not enough water.")
    elif milk_remaining < 0:
        print("Sorry there is not enough milk.")
    elif coffee_remaining < 0:
        print("Sorry there is not enough coffee.")


#---------- COFFEE MACHINE LOGIC ----------#

def start_coffee_machine():
    while True:
        user_choice = get_choice("\nWhat would you like? (espresso/latte/cappuccino): ")
        if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
            check_resources(user_choice)
        elif user_choice == "report":
            get_report()
        elif user_choice == "off":
            break

#---------- ENTRY POINT ----------#

if __name__ == "__main__":
    start_coffee_machine()