from turtle import Turtle, Screen
import random


#---------- CONSTANTS ----------#

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_X = -230
START_Y = -100   
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
TURTLE_SPACING = 40
# Turtle is 40 x 40 (uses centre point), so right edge of screen at (SCREEN_WIDTH / 2) - (TURTLE_SIZE / 2) = 230
FINISH_LINE_X = (SCREEN_WIDTH // 2) - (40 // 2) 


#---------- INITIALISE SCREEN ----------#

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)


#---------- HELPER FUNCTION ----------#

def get_user_bet(title, prompt):
    """Prompt user for colour choice, case-insensitive."""
    while True:
        choice = screen.textinput(title=title, prompt=prompt)
        if choice:
            choice = choice.strip().lower()
            if choice in COLOURS:
                return choice
        print(f"Invalid input. Please enter one of: {', '.join(COLOURS)}.")


#---------- TURTLE RACE FUNCTIONS ----------#

def setup_turtles(colours):
    """Create turtles of given colours, spaced vertically at the left edge of the screen."""
    turtles = {}
    y = START_Y
        
    for colour in colours:
        turtle = Turtle(shape="turtle")
        turtle.color(colour)
        turtle.penup()
        turtle.goto(x=START_X, y=y)
        turtles[colour] = turtle
        y += TURTLE_SPACING
    
    return turtles


def run_race(turtles, user_bet):
    while True:
        for colour, turtle in turtles.items():
            if turtle.xcor() > FINISH_LINE_X:
                result = "won" if colour == user_bet else "lost"
                print(f"You {result}! The {colour} turtle is the winner!")
                return
            turtle.forward(random.randint(0, 10))


#---------- MAIN PROGRAM ----------#

def start_turtle_race():
    user_bet = get_user_bet("Make your bet", "Which turtle will win the race? Enter a colour: ")
    turtles = setup_turtles(COLOURS)
    run_race(turtles, user_bet)


#---------- ENTRY POINT ----------#

if __name__ == "__main__":
    start_turtle_race()
    screen.exitonclick()