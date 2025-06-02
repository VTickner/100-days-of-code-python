from turtle import Turtle, Screen


#---------- CONSTANTS ----------#

STEP = 10
TURN_ANGLE = 15
KEYS_TO_START = ["w", "s", "a", "d", "c", "Up", "Down", " "]


#---------- INITIALISE SCREEN ----------#

screen = Screen()


#---------- HELPER FUNCTIONS ----------#

def is_on_screen(x: float, y: float) -> bool:
    """Check whether turtle is within screen boundaries. Center position is (0,0) so edges are half width/height."""
    half_width = screen.window_width() / 2
    half_height = screen.window_height() / 2
    return -half_width < x < half_width and -half_height < y < half_height


def try_move(turtle: Turtle, move_func, undo_func) -> None:
    """Move the turtle by STEP using move_func(). If off-screen, revert move using undo_func()."""
    move_func(STEP)
    x, y = turtle.pos()
    if not is_on_screen(x, y):
        undo_func(STEP * 3)


#---------- UI DISPLAY FUNCTIONS ----------#

def show_instructions(writer: Turtle) -> None:
    """Display initial instructions using a hidden turtle."""
    writer.hideturtle()
    writer.penup()

    instructions = [
        ("Welcome to Etch-A-Sketch!", 100, 16, "bold"),
        ("Controls:", 60, 12, "normal"),
        ("W - Move forward | S - Move backward", 30, 10, "normal"),
        ("A - Turn left | D - Turn right", 10, 10, "normal"),
        ("C - Clear screen", -10, 10, "normal"),
        ("Up arrow - Pen up | Down arrow - Pen down", -30, 10, "normal"),
        ("Press any key to start drawing...", -70, 10, "italic"),  
    ]
    
    for text, y, size, style in instructions:
        writer.goto(0, y)
        writer.write(arg=text, align="center", font=("Arial", size, style))


def clear_instructions(writer: Turtle, sketcher: Turtle) -> None:
    """Clear instructions and activate drawing controls."""
    writer.clear()
    sketcher.showturtle()
    sketcher.pendown()
    initialise_controls(sketcher)


#---------- CONTROL LOGIC ----------#

def initialise_controls(sketcher: Turtle) -> None:
    """Assign Etch A Sketch keys to control the turtle"""

    def move_forward():
        try_move(sketcher, sketcher.forward, sketcher.backward)


    def move_backward():
        try_move(sketcher, sketcher.backward, sketcher.forward)


    def turn_left():
        sketcher.left(TURN_ANGLE)


    def turn_right():
        sketcher.right(TURN_ANGLE)

    
    def pen_up():
        sketcher.penup()
    

    def pen_down():
        sketcher.pendown()


    def clear_screen():
        sketcher.reset()

    screen.onkeypress(fun=move_forward, key="w")
    screen.onkeypress(fun=move_backward, key="s")
    screen.onkeypress(fun=turn_left, key="a")
    screen.onkeypress(fun=turn_right, key="d")
    screen.onkeypress(fun=pen_up, key="Up")
    screen.onkeypress(fun=pen_down, key="Down")
    screen.onkeypress(fun=clear_screen, key="c")
    screen.listen()


#---------- MAIN PROGRAM ----------#

def begin_drawing(writer: Turtle, sketcher: Turtle) -> None:
    """Unbind setup keys and begin drawing"""
    for key in KEYS_TO_START:
        screen.onkeypress(fun=None, key=key)
    clear_instructions(writer, sketcher)


def main():
    writer = Turtle()
    sketcher = Turtle()
    sketcher.hideturtle()
    sketcher.penup()

    show_instructions(writer)

    def start_handler() -> None:
        begin_drawing(writer, sketcher)

    for key in KEYS_TO_START:
        screen.onkeypress(fun=start_handler, key=key)

    screen.listen()
    screen.exitonclick()


if __name__ == "__main__":
    main()