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

def get_user_bet(writer: Turtle, title, prompt):
    """Prompt user for colour choice, case-insensitive."""
    while True:
        choice = screen.textinput(title=title, prompt=prompt)
        if choice:
            choice = choice.strip().lower()
            if choice in COLOURS:
                writer.clear()
                return choice
        show_message(writer, f"Invalid input. Please enter one of: {', '.join(COLOURS)}.")


#---------- UI DISPLAY FUNCTIONS ----------#

def show_instructions(writer: Turtle) -> None:
    """Display initial instructions using a hidden turtle."""
    writer.hideturtle()
    writer.penup()

    instructions = [
        ("Welcome to Turtle Race!", 100, 16, "bold"),
        ("Place your bet on a colour:", 60, 12, "normal"),
        ("Red | Orange | Yellow | Green | Blue | Purple", 30, 10, "normal"),
        ("Press any key to start the race...", -70, 10, "italic"),  
    ]
    
    for text, y, size, style in instructions:
        writer.goto(0, y)
        writer.write(arg=text, align="center", font=("Arial", size, style))


def clear_instructions(writer: Turtle) -> None:
    """Clear instructions display."""
    writer.clear()


def show_message(writer: Turtle, message: str) -> None:
    """Display a message."""
    writer.penup()
    writer.goto(x=0, y=100)
    writer.write(arg=message, align="center", font=("Arial", 10, "bold"))
    writer.hideturtle()


def show_result(writer: Turtle, winner: str, user_bet: str):
    result = "won" if winner == user_bet else "lost"
    show_message(writer, f"You {result}! The {winner} turtle is the winner!")


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


def run_race(turtles) -> str:
    while True:
        for colour, turtle in turtles.items():
            if turtle.xcor() > FINISH_LINE_X:
                for racer in turtles.values():
                    racer.clear()
                    racer.hideturtle()
                return colour
            turtle.forward(random.randint(0, 10))


#---------- MAIN PROGRAM ----------#

def start_turtle_race():
    """Clear instructions, prompt bet and start race."""
    clear_instructions(writer)

    while True:
        user_bet = get_user_bet(writer, "Make your bet", "Which turtle will win the race? Enter a colour: ")
        turtles = setup_turtles(COLOURS)
        winner = run_race(turtles)
        show_result(writer, winner, user_bet)

        again = screen.textinput("Race Again?", "Would you like to race again? (yes/no): ")
        if not again or again.strip().lower() not in ["yes", "y"]:
            writer.clear()
            show_message(writer, "Thanks for playing!")
            break
        writer.clear()


def main():
    global writer

    writer = Turtle()
    show_instructions(writer)

    screen.listen()
    screen.onkeypress(start_turtle_race)
    screen.exitonclick()


if __name__ == "__main__":
    main()