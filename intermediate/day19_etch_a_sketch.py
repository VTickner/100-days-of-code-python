from turtle import Turtle, Screen


#---------- CONSTANTS ----------#

STEP = 10           # Distance to move
TURN_ANGLE = 15     # Degrees to turn


#---------- INITIALISE TURTLE & SCREEN ----------#

tim = Turtle()
screen = Screen()


#---------- HELPER FUNCTIONS ----------#

def is_on_screen(x, y):
    """Check whether turtle is within screen boundaries. Center position is (0,0) so edges are half width/height."""
    half_width = screen.window_width() / 2
    half_height = screen.window_height() / 2
    return -half_width < x < half_width and -half_height < y < half_height


def try_move(move_func, undo_func):
    """
    Moves by STEP using move_func(), if off-screen, revert move by STEP using undo_func().
    Acts as a reusable check to prevent the turtle from moving outside the visible area.
    """
    move_func(STEP)
    x, y = tim.pos()
    if not is_on_screen(x, y):
        undo_func(STEP * 2)


#---------- DRAWING FUNCTIONS ----------#

def move_forward():
    try_move(tim.forward, tim.backward)


def move_backward():
    try_move(tim.backward, tim.forward)


def turn_left():
    tim.left(TURN_ANGLE)


def turn_right():
    tim.right(TURN_ANGLE)


def clear_screen():
    tim.reset()


#---------- MAIN PROGRAM ----------#

screen.listen()
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=turn_right, key="d")
screen.onkeypress(fun=clear_screen, key="c")


#---------- KEEP WINDOW OPEN ----------#

screen.exitonclick()