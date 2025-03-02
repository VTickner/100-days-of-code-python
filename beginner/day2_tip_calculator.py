print("Welcome to the tip calculator!")

while True:
    total_bill = input("What was the total bill? $")
    try:
        total_bill = float(total_bill)
        if total_bill < 1:
            print("The bill cannot be 0 or less")
        else:
            break
    except ValueError:
        print("Please enter a valid number")

while True:
    tip = input("How much would you like to give? 10, 12 or 15? ")
    try:
        tip = float(tip)
        if tip not in [10, 12, 15]:
            print("Please enter either 10, 12 or 15 for the tip amount.")
        else:
            tip = tip / 100
            break
    except ValueError:
        print("Please enter a valid number")

while True:
    number_people = input("How many people to split the bill? ")
    try:
        number_people = int(number_people)
        if number_people < 1:
            print("The number of people cannot be 0 or less")
        else:
            break
    except ValueError:
        print("Please enter a valid number")

payment_per_person = round((total_bill + total_bill * tip) / number_people, 2)
print(f"Each person should pay: ${payment_per_person:.2f}")