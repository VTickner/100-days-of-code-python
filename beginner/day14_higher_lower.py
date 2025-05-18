import random
from higher_lower_art import logo, vs
from higher_lower_data import data


#---------- INPUT HANDLERS ----------#

def get_choice(prompt, valid_inputs):
    """Prompt for either: 'A' or 'B', or either: 'Y' or 'N', case-insensitive."""
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_inputs:
            return choice
        print(f"Invalid input. Please enter either '{valid_inputs[0]}' or '{valid_inputs[1]}'.")


#---------- DATA HANDLERS ----------#

def get_random_item():
    return random.choice(data)


def get_comparison_item(item):
    """Return a different item from the one provided."""
    while True:
        comparison_item = get_random_item()
        if comparison_item != item:
            return comparison_item


def format_item_info(item, option):
    return f"Compare {option}: {item['name']}, a {item['description']}, from {item['country']}"


def compare_follower_counts(item_a, item_b):
    """Compare two items and return 'A' if item_a has more followers, else 'B'."""
    return "A" if item_a['follower_count'] > item_b['follower_count'] else "B"


#---------- GAME LOGIC ----------#

def play_game():
    print("\n" + logo)
    score = 0
    item_a = get_random_item()

    while True:
        item_b = get_comparison_item(item_a)
        print(format_item_info(item_a, "A"))
        print(vs)
        print(format_item_info(item_b, "B"))

        correct_answer = compare_follower_counts(item_a, item_b)
        user_guess = get_choice("Who has more followers? Type 'A' or 'B': ", ["A", "B"])

        if user_guess == correct_answer:
            score += 1
            print("\n" + logo)
            print(f"You're right! Current score: {score}")
            item_a = item_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break


def start_higher_lower():
    while True:
        play_game()
        if get_choice("\nDo you want to play another Higher Lower game? Type 'Y' or 'N': ", ["Y", "N"]) == 'N':
            print("Thanks for playing. Goodbye!")
            break


#---------- ENTRY POINT ----------#

if __name__ == "__main__":
    start_higher_lower()