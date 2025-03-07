import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def get_input_quantity(password_question):
    while True:
        try:
            return int(input(password_question))
        except ValueError:
            print("Please enter a valid number")

def generate_password_section(quantity, password_section, password):
    for _ in range(0, quantity):
        password.append(random.choice(password_section))

print("Welcome to the PyPassword Generator!")
nr_letters = get_input_quantity("How many letters would you like in your password?\n")
nr_numbers = get_input_quantity("How many numbers would you like?\n")
nr_symbols = get_input_quantity("How many symbols would you like?\n")

password = []
generate_password_section(nr_letters, letters, password)
generate_password_section(nr_numbers, numbers, password)
generate_password_section(nr_symbols, symbols, password)

random.shuffle(password)
print(f"Here is your password: {''.join(password)}")