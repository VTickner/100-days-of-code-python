import random
from guess_the_number_art import logo

#---------- INPUT HANDLERS ----------#

def get_level(prompt):
    """Prompt for 'easy' or 'hard', case-insensitive"""
    while True:
        level = input(prompt).strip().lower()
        if level in ("easy", "hard"):
            return level
        print("Invalid input. Please enter either 'easy' or 'hard'.")


def get_number(prompt):
    """Prompt for number between 1 and 100 (inclusive)"""
    while True: 
        try:
            number = int(input(prompt))
            if 1 <= number <= 100:
                return number
            else:
                print("Number must be between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_y_n(prompt):
    """Prompt for 'y' or 'n', case-insensitive"""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "n"):
            return choice
        print("Invalid input. Please enter either 'y' or 'n'.")


#---------- GUESS THE NUMBER ----------#

def get_attempts_by_level():
    level = get_level("\nChoose a difficulty. Type 'easy' or 'hard': ")
    return 10 if level == "easy" else 5


def player_guesses(attempts, target):
    while attempts > 0:
        print(f"You have {attempts} attempt{'s' if attempts != 1 else ''} remaining to guess the number.")
        guess = get_number("Make a guess: ")
        attempts -= 1

        if guess == target:
            print(f"You got it! The answer was {target}")
            return
        
        if attempts == 0:
            break
        
        if guess > target:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")
    
    print(f"You've run out of guesses. The number was {target}.")


def start_game():
    print("\n" + logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    target_number = random.randint(1, 100)
    # print(target_number) # uncomment for testing

    attempts = get_attempts_by_level()
    player_guesses(attempts, target_number)


def play_guess_number():
    while True:
        start_game()
        if get_y_n("\nDo you want to play another Guess The Number game? Type 'y' or 'n': ") == 'n':
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    play_guess_number()