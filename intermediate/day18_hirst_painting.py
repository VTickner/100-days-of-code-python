from turtle import Turtle, Screen
import random


#---------- EXTRACT COLOURS FROM IMAGE ----------#

# import colorgram

# Extract colours from image only need to do once
# colours = colorgram.extract("intermediate/image.jpg", 30)
# rgb_colours = [(colour.rgb.r, colour.rgb.g, colour.rgb.b) for colour in colours]
# print(rgb_colours)

# A manually saved list of colours copied from rgb_colours print output
COLOUR_LIST = [
    (195, 177, 148), (159, 186, 177), (165, 184, 193), (198, 170, 180), (211, 196, 145), (205, 185, 184),
    (196, 204, 200), (221, 213, 215), (201, 186, 189), (185, 195, 192), (194, 198, 200), (187, 193, 195), 
    (191, 191, 194), (131, 123, 112), (135, 129, 116), (137, 125, 120),
]

DOT_ROWS = 10
DOT_COLUMNS = 10
DOT_SIZE = 20
DOT_SPACING = 50
START_OFFSET = 18   


#---------- SETUP SCREEN ----------#

screen = Screen()
screen.colormode(255)  # <-- important: enable RGB 0-255 mode


#---------- DRAWING FUNCTION ----------#

def draw_dot_grid():
    tim = Turtle()
    tim.penup()
    tim.hideturtle()
    tim.speed("fastest")

    # Move to starting position (bottom left of grid)
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)

    for _ in range(DOT_ROWS):
        for _ in range(DOT_COLUMNS):
            tim.dot(DOT_SIZE, random.choice(COLOUR_LIST))
            tim.forward(DOT_SPACING)

        tim.setheading(90)
        tim.forward(DOT_SPACING)
        tim.setheading(180)
        tim.forward(DOT_SPACING * DOT_COLUMNS)
        tim.setheading(0)


#---------- RUN PROGRAM ----------#

draw_dot_grid()

#---------- KEEP WINDOW OPEN ----------#

screen.exitonclick()