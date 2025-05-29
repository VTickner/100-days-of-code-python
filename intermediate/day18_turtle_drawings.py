from turtle import Turtle, Screen
import random

#---------- CONSTANTS ----------#

COLOURS = [
    "DarkOrchid", "DarkOrchid1", "DarkOrchid2", "DarkOrchid3", "DarkOrchid4", "MediumOrchid", "MediumOrchid1", "MediumOrchid2", "MediumOrchid3", "MediumOrchid4", "orchid", "orchid1", "orchid2", "orchid3", "orchid4"
]
DIRECTIONS = [0, 90, 180, 270]
SHAPE_SIZE = 100
STEP_LENGTH = 10
STEP_COUNT = 15
WALK_STEPS = 200


#---------- INITIALISE TURTLE ----------#

tim = Turtle()
tim.shape("turtle")
tim.color("DarkOrchid4")
tim.speed("fastest")


#---------- DRAWING FUNCTIONS ----------#

def change_position(x: float, y: float) -> None:
    """Clear screen and move turtle to a new position."""
    tim.clear()
    tim.penup()
    tim.setpos(x, y)
    tim.pendown()


def draw_regular_polygon(sides: int, length: float) -> None:
    """Draw a regular polygon with the given number of sides and side length"""
    angle = 360 / sides

    for _ in range(sides):
        tim.forward(length)
        tim.right(angle)


def draw_square():
    """Draw a square using turtle."""
    change_position(0.0, 0.0)
    draw_regular_polygon(4, SHAPE_SIZE)


def draw_dashed_line():
    """Draw a dashed line using turtle."""
    change_position(-150.0, 0.0)

    for _ in range(STEP_COUNT):
        tim.forward(STEP_LENGTH)
        tim.penup()
        tim.forward(STEP_LENGTH)
        tim.pendown()


def draw_multiple_shapes():
    """Draw multiple shapes laid over each other from triangle to nonagon, each in a random colour."""
    change_position(0.0, 0.0)

    for sides in range(3, 10):
        tim.color(random.choice(COLOURS))
        draw_regular_polygon(sides, SHAPE_SIZE)


def draw_random_walk():
    """Draw a random walk using thick random coloured lines."""
    change_position(0.0, 0.0)
    tim.pensize(10)

    for _ in range(WALK_STEPS):
        tim.color(random.choice(COLOURS))
        tim.forward(STEP_LENGTH * 3)
        tim.setheading(random.choice(DIRECTIONS))
    
    tim.pensize(1)


def draw_spirograph(gap_size):
    """Draw a spirograph in random colours by rotating circles."""
    change_position(0.0, 0.0)

    for _ in range(int(360 / gap_size)):
        tim.color(random.choice(COLOURS))
        tim.circle(SHAPE_SIZE)
        tim.setheading(tim.heading() + gap_size)


#---------- MAIN PROGRAM ----------#

draw_square()
draw_dashed_line()
draw_multiple_shapes()
draw_random_walk()
draw_spirograph(5)


#---------- KEEP WINDOW OPEN ----------#

screen = Screen()
screen.exitonclick()