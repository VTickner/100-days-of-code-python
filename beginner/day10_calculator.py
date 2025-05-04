from calculator_art import logo

# ---------- OPERATION FUNCTIONS ---------- #

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        print("Error: Cannot divide by zero.")
        return None
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# ---------- INPUT HANDLERS ----------#

def get_number(prompt):
    while True: 
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_operation():
    while True: 
        operation = input("+\n-\n*\n/\nPick an operation: ").strip()
        if operation in operations:
            return operation
        print("Invalid input. Please enter +, -, * or /.")


def get_continue_choice(result):
    while True:
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").strip().lower()
        if choice in ("y", "n"):
            return choice
        print("Invalid input. Please enter either 'y' or 'n'.")


# --------- CALCULATOR LOGIC ----------#

def calculator():
    print(logo)
    
    #  handles starting a new calculation
    while True:
        use_result = True
        num1 = get_number("What's the first number?: ")
        
        # handles chaining operations on the result
        while use_result:
            operation = get_operation()
            num2 = get_number("What's the next number?: ")
            result = operations[operation](num1, num2)
            
            if result is None:
                continue  # skip displaying print message for division by zero

            print(f"{num1} {operation} {num2} = {result}")
            
            if get_continue_choice(result) == 'y':
                num1 = result  # continue with result
            else:
                use_result = False
                calculator()


# ---------- RUN THE CALCULATOR ----------#

calculator()