# 100 Days Of Code: The Complete Python Pro Bootcamp

These projects were created as part of [Dr. Angela Yu's "100 Days of Code: The Complete Python pro Bootcamp"](https://www.udemy.com/course/100-days-of-code) course on Udemy.

(Latest projects are added to the top of the list.)

## Table of Contents

- [Beginner](#beginner)
  - [Day 7 - Hangman](#day-7---hangman)
  - [Day 6 - Day 6 - Python Functions & Karel](#day-6---python-functions--karel)
  - [Day 5 - Python Loops](#day-5---python-loops)
  - [Day 4 - Randomisation and Python Lists](#day-4---randomisation-and-python-lists)
  - [Day 3 - Control Flow and Logical Operators](#day-3---control-flow-and-logical-operators)
  - [Day 2 - Understanding Data Types and How to Manipulate Strings](#day-2---understanding-data-types-and-how-to-manipulate-strings)
  - [Day 1 - Working with Variables in Python to Manage Data](#day-1---working-with-variables-in-python-to-manage-data)
- [Other](#other)
  - [Tools and Technologies Used](#tools-and-technologies-used)
  - [Author](#author)

# Beginner

## Day 7 - Hangman

### Project requirements

- Create a flowchart showing how the hangman game works.
- Build a Hangman game:
  - Print the logo from `hangman_art.py`.
  - Randomly choose a word from the `word_list` (from `hangman_words.py`) and assign it to a variable called `chosen_word`.
  - Ask the user to guess a letter and assign their answer to a variable called `guess`.
  - Check if the letter the user guessed `guess` is one of the letters in the `chosen_word`.
  - Create an empty String called `placeholder`.
    - For each letter in the `chosen_word`, add a \_ to placeholder so each `\_ represents a letter to guess.
  - Create an empty string called "display".
    - Loop through each letter in the chosen_word. If the letter at that position matches guess then reveal that letter in the display at that position.
  - Use a while loop to let the user guess again.
    - The loop should only stop once the user has guessed all the letters in the `chosen_word` and no \_ left.
    - The for loop is to be updated so that previous guesses are added to the `display` string and the previous correct letters will also be printed out.
    - Tell the user they've won.
  - Create a variable called `lives` to keep track of the number of lives left - initialise with 6 lives.
  - If guess is not a letter in the chosen_word, then reduce lives by 1.
    - If lives goes down to 0 then the game should end, and it should print "You lose."
  - If the user has entered a letter they've already guessed, print the letter and let them know. User does not lose a life.
  - Print the ASCII art from the list `stages` (from `hangman_words.py`) that corresponds to the current number of `lives` the user has remaining.
  - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
  - Tell the user how many lives they have left.
  - Tell the user the correct word they were trying to guess.

### Code & Potential Improvements:

Flowchart to show how the logic of hangman will work:
![Hangman Flowchart](./Hangman_flowchart.jpg)

- Solution URL: [Day 7 - Hangman](./beginner/day7_hangman.py)
- Incorrect guesses that have already been previously guessed do not lose another life. This is done by adding all incorrect guesses to `incorrect_letters` and checking guesses against incorrect letters to see whether the user loses a life or not.

## Day 6 - Python Functions & Karel

### Project requirements

[Reeborg](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json) was exploring a dark maze and the battery in its flashlight ran out.

Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

### Code & Potential Improvements:

- Solution URL: [Day 6 - Escaping The Maze](./beginner/day6_escaping_the_maze.txt)
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

- Solution URL: [Day 5 - Password Generator](./beginner/day5_password_generator.py)
- I defined a function `get_input_quantity(password_question)` to obtain the answers to the questions posed to the user. This function uses `while True`, along with `try / except ValueError` to check the inputs to the user questions are valid numbers.
- I defined a function `generate_password_section(quantity, password_section, password)` to obtain the appropriate amount of letters, numbers and symbols as requested by the user. Using `random.choice(password_section)` to randomly pick an item from the appropriate list.
- Once the password is generated,`random.shuffle()` is used to mix up the letters, numbers and symbols in the password.

## Day 4 - Randomisation and Python Lists

### Project requirements

- Build a Rock Paper Scissors game.

### Code & Potential Improvements:

- Solution URL: [Day 4 - Rock Paper Scissors](./beginner/day4_rock_paper_scissors.py)
- I used a list to hold the ascii art variables to allow selection of rock, paper, scissors choices.
- I used `while True`, along with `try / except ValueError` and `if user_choice not in [0, 1, 2]` to check whether the user's choice was 0 (rock), 1 (paper), 2 (scissors).
- `import random` with `computer_choice = random.randint(0,2)` was used to generate a random choice for the computer.
- I used `if / elif` statements to compare the user and computer's choices to see who won the game.

## Day 3 - Control Flow and Logical Operators

### Project requirements:

- Build a "Chose your own adventure game".
- Use the [flow chart](https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D) linked to create the game logic for the adventure game.

  <img src="./treasure_island_conditional.jpg" width="500">

### Code & Potential Improvements:

- Solution URL: [Day 3 - Treasure Island](./beginner/day3_treasure_island.py)
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

- Solution URL: [Day 2 - Tip Calculator](./beginner/day2_tip_calculator.py)
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

- Solution URL: [Day 1 - Band Name Generator](./beginner/day1_band_name_generator.py)
- I used `while True` and `if` statements to check whether an empty string had been entered for the city and pet names and if so to request the input again from the user.

# Other

## Tools and Technologies Used

- Python
- PyCharm

## Author

- V. Tickner
