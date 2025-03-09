import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
# print(f"The solution is: {chosen_word}") # used when testing

placeholder = ""
word_length = len(chosen_word)
for position in range (word_length):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

lives = 6
game_over = False
correct_letters = []
incorrect_letters =[]

while not game_over:

    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    display = ""
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(f"Word to guess: {display}")

    if guess not in chosen_word:
        if guess in incorrect_letters:
            print(f"You already guessed {guess}, that's not in the word.")
        else:
            incorrect_letters.append(guess)
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            if lives == 0:
                game_over = True
                print(f"*********************** IT WAS {chosen_word}! YOU LOSE **********************")

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")
    
    print(stages[lives])