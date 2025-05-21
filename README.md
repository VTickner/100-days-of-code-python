100 Days Of Code: The Complete Python Pro Bootcamp

These projects were created as part of [Dr. Angela Yu's "100 Days of Code: The Complete Python pro Bootcamp"](https://www.udemy.com/course/100-days-of-code) course on Udemy.

(Latest projects are added to the top of the list.)

## Table of Contents

- [Intermediate](#intermediate)
  - [Day 15 - Local Development Environment Setup & the Coffee Machine](#day-15---local-development-environment-setup--the-coffee-machine)
- [Beginner](#beginner)
  - [Day 14 - Higher Lower Game Project](#day-14---higher-lower-game-project)
  - [Day 13 - Debugging: How to Find and Fix Errors in Your Code](#day-13---debugging-how-to-find-and-fix-errors-in-your-code)
  - [Day 12 - Scope & Number Guessing Game](#day-12---scope--number-guessing-game)
  - [Day 11 - The Blackjack Capstone Project](#day-11---the-blackjack-capstone-project)
  - [Day 10 - Functions with Outputs](#day-10---functions-with-outputs)
  - [Day 9 - Dictionaries, Nesting and the Secret Auction](#day-9---dictionaries-nesting-and-the-secret-auction)
  - [Day 8 - Function Parameters & Caesar Cipher](#day-8---function-parameters--caesar-cipher)
  - [Day 7 - Hangman](#day-7---hangman)
  - [Day 6 - Python Functions & Karel](#day-6---python-functions--karel)
  - [Day 5 - Python Loops](#day-5---python-loops)
  - [Day 4 - Randomisation and Python Lists](#day-4---randomisation-and-python-lists)
  - [Day 3 - Control Flow and Logical Operators](#day-3---control-flow-and-logical-operators)
  - [Day 2 - Understanding Data Types and How to Manipulate Strings](#day-2---understanding-data-types-and-how-to-manipulate-strings)
  - [Day 1 - Working with Variables in Python to Manage Data](#day-1---working-with-variables-in-python-to-manage-data)
- [Other](#other)
  - [Tools and Technologies Used](#tools-and-technologies-used)
  - [Author](#author)

# Intermediate

## Day 15 - Local Development Environment Setup & the Coffee Machine

Coffee Machine Program Requirements:

1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
   a. Check the user’s input to decide what to do next.
   b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “off” to the prompt.
   a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. The code should end execution when this happens.
3. Print report.
   a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
   Water: 100ml
   Milk: 50ml
   Coffee: 76g
   Money: $2.5
4. Check resources sufficient?
   a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
   b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
   c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
   a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
   b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
   c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
   a. Check that the user has inserted enough money to purchase the drink they selected.
   E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
   b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
   Water: 100ml
   Milk: 50ml
   Coffee: 76g
   Money: $2.5
   c. If the user has inserted too much money, the machine should offer change.
   E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
7. Make Coffee.
   a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
   E.g. report before purchasing latte:
   Water: 300ml
   Milk: 200ml
   Coffee: 100g
   Money: $0
   Report after purchasing latte:
   Water: 100ml
   Milk: 50ml
   Coffee: 76g
   Money: $2.5
   b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.

### Code & Potential Improvements:

Solution URL: [Day 15 - Coffee Machine](./intermediate/coffee_machine.py)

# Beginner

## Day 14 - Higher Lower Game Project

Build a Higher Lower Game where the player must guess which of two options has the higher follower count.

Game Features:

- Score points for every correct guess.
- Randomly choose two different items to compare (must not be the same item).
- When the player guesses correctly, move option B to option A and randomly generate a new option B.
- When the player guesses incorrectly, the game ends.

### Code & Potential Improvements:

I created the following flowchart to outline the game's logic and flow:

![Higher Lower Game Flowchart](./beginner/higher_lower_flowchart.jpg)

Solution URL: [Day 14 - Higher Lower Game](./beginner/day14_higher_lower.py)

Input Handling:

- Added a reusable input validation function: `get_choice()`
  - Ensures input is `A` or `B` (used for player guesses), or `Y` or `N` (used to replay the game)

Data Handling functions:

- `get_random_item()` - retrieves a random item from [higher_lower_data.py](./beginner/higher_lower_data.py)
- `get_comparison_item(item)` - ensures the second item is different from the first.
- `format_item_info()` - formats for display item information clearly to the user.
- `compare_follower_accounts(item_a, item_b)` - compares follower counts and returns the correct choice (`A` or `B`).

Game logic:

- `play_game()` - runs each game session, handles comparison logic and tracks scoring.
- `start_higher_lower()` - manages replay functionality.

## Day 13 - Debugging: How to Find and Fix Errors in Your Code

Day 13 focused on various debugging techniques and how to use a debugger tool.

## Day 12 - Scope & Number Guessing Game

Build a Number Guessing Game where the player must guess a randomly chosen number between 1 and 100.

Game Features:

- Two difficulty levels:
  - Easy level - 10 attempts to guess number.
  - Hard level - 5 attempts to guess number.
- After each incorrect guess (if attempts remain), the player is told whether their guess was too high or too low.

### Code & Potential Improvements:

Before writing the code, I created the following flowchart to outline the game's logic and flow:

![Guess The Number Flowchart](./beginner/guess_the_number_flowchart.jpg)

Solution URL: [Day 12 - Number Guessing Game](./beginner/day12_guess_the_number.py)

- Added input validation functions.
  - `get_level()` - ensures input is `easy` or `hard`
  - `get_number()` - ensures input is a number between 1 and 100
  - `get_y_n()` - ensures input is `y` or `n`
- Added play again functionality.
- Game logic separated into different functions for readability and modularity:
  - `get_attempts_by_level()` - sets attempts based on chosen level.
  - `player_guesses(attempts, target)` - handles guess checking and feedback to the player.
  - `start_game()` - initialises each game round.
  - `play_guess_number()` - handles play again logic.
- A potential improvement would be to add a scoring system that tracks wins/losses or records fewest guesses used to win (high score).

## Day 11 - The Blackjack Capstone Project

### Blackjack Game House Rules

Build a Blackjack game with the following rules:

- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards:
  `cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.

### Code & Potential Improvements:

I created this flowchart to visualise the game logic before coding:

![Blackjack Flowchart](./beginner/blackjack_flowchart.jpg)

Solution URL: [Day 11 - Blackjack](./beginner/day11_blackjack.py)

- Added input handling:
  - `get_choice(prompt)` - ensures input is `y` or `n`
- Broke the game into dedicated functions for each task:
  - `change_ace_score(hand)`
  - `show_final_cards(player, dealer)`
  - `bust(hand, player, dealer)`
  - `player_turn(player, dealer)`
  - `dealer_turn(dealer)`
  - `compare_scores(player_score, dealer_score)`
  - `start_game()`
  - `play_blackjack()`
- Refactored for clarity and maintainability:
  - Renamed variables and functions for clearer meaning e.g. `cards` -> `card_values`.
  - Reduced function parameters by calculating `player_score` and `dealer_score` inside the relevant functions.
  - Extracted specific tasks into smaller, purpose-specific functions:
    - `deal_initial_cards()` - handles card dealing.
    - `check_blackjack(player, dealer)` checks if either player or dealer hits blackjack.
  - Added a reusable helper function for detecting blackjack:
    ```python
    def has_blackjack(hand):
      return sum(hand) == 21 and len(hand) == 2
    ```
  - Ensured `player_turn()` and `dealer_turn()` both return `(score, is_bust)` to maintain consistency.
  - Moved blackjack checks out of `compare_scores()` and into `check_blackjack()`.
  - Simplified `start_game()` so the sequence of gameplay is easier to follow: deal cards, check for blackjack, player's turn, dealer's turn, check for busts, compare scores.

## Day 10 - Functions with Outputs

Build a calculator program:

- Use functions to to calculate add, subtract, multiply and divide.
- Have a dictionary store keys for +, -, \*, / and values as the corresponding functions.
- Use the dictionary to perform the calculations.
- Program asks the user to type the first number.
- Program asks the user to type a mathematical operator (a choice of `+`, `-`, `*` or `/`)
- Program asks the user to type the second number.
- Program works out the result based on the chosen mathematical operator.
- Program asks if the user wants to continue working with the previous result.
- If yes, program loops to use the previous result as the first number and then repeats the calculation process.
- If no, program asks the user for the fist number again and wipes all memory of previous calculations.
- Add the logo from `calculator_art.py`.

### Code & Potential Improvements:

Solution URL: [Day 10 - Calculator](./beginner/day10_calculator.py)

- Added input checking:
  - `get_number()` uses `while True`, along with `try / except ValueError` to ensure only numbers have been entered.
  - `get_operation()` uses `while True` to ensure only valid calculator operators have been entered.
  - `get_continue_choice()` uses `while True`to ensure either `y` or `n` has been entered.

## Day 9 - Dictionaries, Nesting and the Secret Auction

Build a blind auction program:

- Use the flowchart to guide the creation of the blind auction program:
  ![Secret Auction Flowchart](./beginner/secret_auction_flowchart.jpg)
- Ask the user for input: name and bid.
- Save the data into a dictionary.
- Check whether new bids need to be entered.
- Compare the bids in the dictionary.

### Code & Potential Improvements:

Solution URL: [Day 9 - Secret Auction](./beginner/day9_secret_auction.py)

- Used `while True`, along with `try / except ValueError` to check the input for the bids are valid numbers.
- If there are other bids, `print("\n" * 20)` was used to create some vertical space for the next bidder to not see the previous bid on the screen.
- Formatted the output of the winning bid to 2dp to keep it consistent with how currency is written: `${max_bid:.2f}`.

## Day 8 - Function Parameters & Caesar Cipher

### Project requirements

- Create a function called `encrypt()` that takes `original_text` and `shift_amount` as two inputs.
  - The function should shift each letter of the `original_text` forwards in the alphabet by the `shift_amount` and print the encrypted text.
- Call the `encrypt()` function and pass in the user inputs. Test the code and encrypt a message.
- Fix the code so that it wraps around to the start of the alphabet if the letter is shifted past z.

- Create a function called `decrypt()` that takes `original_text` and `shift_amount` as inputs.
  - The function should shift each letter of the `original_text` **backwards** in the alphabet by the `shift_amount` and print the decrypted text.

As the `encrypt()` and `decrypt()` functions are so similar:

- Combine them into one function called `caesar()`.
  - Use the value of the user chosen `direction` variable to determine which functionality to use.
- Call the caesar function instead of `encrypt()`/`decrypt()` and pass in all three variables `direction`/`text`/`shift`.

- Import and print the logo from `caesar_art.py` when the program starts.
- Deal with if the user enters a number/symbol/space.
- Add the ability to restart the cipher program again

### Code & Potential Improvements:

Solution URL: [Day 8 - Caesar Cipher](./beginner/day8_caesar_cipher.py)

- When calling `caesar()` I ensured it was very clear what variables belonged to which parameters by using named arguments: `caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)`. This makes the function call more readable and avoids confusion, especially when a function has multiple parameters.

## Day 7 - Hangman

### Project requirements

- Create a flowchart showing how the hangman game works.
- Build a Hangman game:
  - Print the logo from `hangman_art.py`.
  - Randomly choose a word from the `word_list` (from `hangman_words.py`) and assign it to a variable called `chosen_word`.
  - Ask the user to guess a letter and assign their answer to a variable called `guess`.
  - Check if the letter the user guessed is one of the letters in the `chosen_word`.
  - Create an empty string called `placeholder`.
    - For each letter in the `chosen_word`, add a \_ to placeholder so each \_ represents a letter to guess.
  - Create an empty string called "display".
    - Loop through each letter in the `chosen_word`. If the letter at that position matches `guess` then reveal that letter in the display at that position.
  - Use a while loop to let the user guess again.
    - The loop should only stop once the user has guessed all the letters in the `chosen_word` and no \_ are left.
    - The for loop is to be updated so that previous guesses are added to the `display` string and the previous correct letters will also be printed out.
    - Tell the user they've won.
  - Create a variable called `lives` to keep track of the number of lives left - initialise with 6 lives.
  - If `guess` is not a letter in the chosen_word, then reduce `lives` by 1.
    - If `lives` goes down to 0 then the game should end, and it should tell the user they've lost.
  - If the user has entered a letter they've already guessed, print the letter and let them know. The user does not lose a life in this case.
  - Print the ASCII art from the list `stages` (from `hangman_words.py`) that corresponds to the current number of `lives` the user has remaining.
  - If the letter is not in the `chosen_word`, print out the letter and let the user know it's not in the word.
  - Tell the user how many `lives` they have left.
  - Tell the user the correct word they were trying to guess.

### Code & Potential Improvements:

Flowchart to show the logic of the Hangman game:
![Hangman Flowchart](./beginner/hangman_flowchart_v2.jpg)

Solution URL: [Day 7 - Hangman](./beginner/day7_hangman.py)

- Incorrect guesses that have already been previously guessed do not lose another life. This is done by adding all incorrect guesses to `incorrect_letters` and checking guesses against `incorrect_letters` to see whether the user loses a life or not.
- Refactored to make more concise and improve readability.
- Added a check on user input to make sure a single letter was entered.
- Updated the flowchart to match changes made to the program. [Click here for the original flowchart](./beginner/hangman_flowchart.jpg).

## Day 6 - Python Functions & Karel

### Project requirements

[Reeborg](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json) was exploring a dark maze and the battery in its flashlight ran out.

Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

### Code & Potential Improvements:

Solution URL: [Day 6 - Escaping The Maze](./beginner/day6_escaping_the_maze.txt)

- As there was no `turn_right()` function, I defined one, using the `turn_left()` function.
- Used the functions `at_goal()`, `right_is_clear()` and `front_is_clear()` to detect where it is possible for Reeborg to move to.

## Day 5 - Python Loops

### Project requirements

The program will ask:

- How many letters would you like in your password?
- How many numbers would you like?
- How many symbols would you like?

The objective is to take the inputs from the user to these questions and then generate a random password, with the letters, numbers and symbols mixed up in the password.

### Code & Potential Improvements:

Solution URL: [Day 5 - Password Generator](./beginner/day5_password_generator.py)

- I defined a function `get_input_quantity(password_question)` to obtain the answers to the questions posed to the user. This function uses `while True`, along with `try / except ValueError` to check the inputs to the user questions are valid numbers.
- I defined a function `generate_password_section(quantity, password_section, password)` to obtain the appropriate amount of letters, numbers and symbols as requested by the user. Using `random.choice(password_section)` to randomly pick an item from the appropriate list.
- Once the password is generated,`random.shuffle()` is used to mix up the letters, numbers and symbols in the password.

## Day 4 - Randomisation and Python Lists

### Project requirements

Build a Rock Paper Scissors game.

### Code & Potential Improvements:

Solution URL: [Day 4 - Rock Paper Scissors](./beginner/day4_rock_paper_scissors.py)

- I used a list to hold the ascii art variables to allow selection of rock, paper, scissors choices.
- I used `while True`, along with `try / except ValueError` and `if user_choice not in [0, 1, 2]` to check whether the user's choice was 0 (rock), 1 (paper), 2 (scissors).
- `import random` with `computer_choice = random.randint(0,2)` was used to generate a random choice for the computer.
- I used `if / elif` statements to compare the user and computer's choices to see who won the game.

## Day 3 - Control Flow and Logical Operators

### Project requirements:

Build a "Chose your own adventure game".

- Use the [flow chart](https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D) linked to create the game logic for the adventure game.

  <img src="./beginner/treasure_island_conditional.jpg" width="500">

### Code & Potential Improvements:

Solution URL: [Day 3 - Treasure Island](./beginner/day3_treasure_island.py)

- I used `if / else` statements to select the user's choice.
- I used a dictionary to hold the ending outcomes of which door the user selected at the end of the adventure game.

## Day 2 - Understanding Data Types and How to Manipulate Strings

### Project requirements:

1. To match how [https://appbrewery.github.io/python-day2-demo/](https://appbrewery.github.io/python-day2-demo/) operates.
2. Ask the user for the total bill amount.
3. Ask the user the tip percentage, choice of 10, 12 or 15%.
4. Ask the user how many people are splitting the bill.
5. Show the amount each person needs to pay, make sure answer is to 2 decimal places.

Example:

- If the bill was $150.00, split between 5 people, with 12% tip.
- Each person should pay: `(150.00 / 5) * 1.12 = 33.6`.
- After formatting the result to 2 decimal places = 33.60

### Code & Potential Improvements:

Solution URL: [Day 2 - Tip Calculator](./beginner/day2_tip_calculator.py)

- I used `while True` and `if` statements to check whether the bill and the number of people splitting the bill are numbers > 0 and if not to request the input again from the user.
- I used `while True` and `if tip not in [10, 12, 15]` to check whether the tip amount was 10, 12 or 15%.
- To get the output to always be to 2 decimal places:
  ```python
  print(f"Each person should pay: ${payment_per_person:.2f}")
  ```

## Day 1 - Working with Variables in Python to Manage Data

### Project requirements:

1. Create a greeting for your program.
2. Ask the user for the city that they grew up in and store it in a variable.
3. Ask the user for the name of a pet and store it in a variable.
4. Combine the name of their city and pet and show them their band name.
5. Make sure the input cursor shows on a new line.

### Code & Potential Improvements:

Solution URL: [Day 1 - Band Name Generator](./beginner/day1_band_name_generator.py)

- I used `while True` and `if` statements to check whether an empty string had been entered for the city and pet names and if so to request the input again from the user.

# Other

## Tools and Technologies Used

- Debugger
- Flowcharts
- Python
- PyCharm

## Author

- V. Tickner
