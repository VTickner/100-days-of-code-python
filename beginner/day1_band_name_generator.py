print("Welcome to the Band Name Generator")

# using while True statements to check text has been entered for city and pet names

while True:
    city_name = input("What's the name of the city you grew up in?\n")
    if city_name == "":
        print("You need to input some text.")
    else:
        break

while True:
    pet_name = input("What's your pet's name?\n")
    if pet_name == "":
        print("You need to input some text.")
    else:
        break

print("Your band name could be " + city_name + " " + pet_name)