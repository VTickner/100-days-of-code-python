import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_images = [rock, paper, scissors]

print("Welcome to the Rock, Paper, Scissors game!")

while True:
    user_choice = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    try:
        user_choice = int(user_choice)
        if user_choice not in [0, 1, 2]:
            print("Please enter either 0, 1 or 2 for your choice.")
        else:
            print(choice_images[user_choice])
            break
    except ValueError:
        print("Please enter a valid number.")

computer_choice = random.randint(0,2)
print(f"Computer choose:\n{choice_images[computer_choice]}")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")