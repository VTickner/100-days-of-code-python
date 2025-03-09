import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
# print(f"The solution is: {chosen_word}") # used when testing

placeholder = "_" * len(chosen_word)
print(f"Word to guess: {placeholder}")

lives = 6
game_over = False
# used sets instead of lists so no repetitions of letters
correct_letters = set()
incorrect_letters = set()

while not game_over:

    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue  # skip rest of loop so no lives are lost for incorrect input

    if guess in correct_letters or guess in incorrect_letters:
        print(f"You've already guessed {guess}")
        continue # skip rest of loop so no lives are lost
    
    if guess in chosen_word:
        correct_letters.add(guess)
    else:
        incorrect_letters.add(guess)
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS {chosen_word}! YOU LOSE **********************")

    display = ''.join(letter if letter in correct_letters else "_" for letter in chosen_word)
    print(f"Word to guess: {display}")

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")
    
    print(stages[lives])