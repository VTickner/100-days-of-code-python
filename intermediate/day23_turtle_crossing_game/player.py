from turtle import Turtle


class Player(Turtle):
    """Turtle for the Turtle Crossing game. Moves only upwards."""

    #---------- CONSTANTS ----------#

    COLOUR: str = "black"
    SHAPE: str = "turtle"
    STARTING_POSITION: tuple[int, int] = (0, -280)
    MOVE_DISTANCE: int = 10 # Distance turtle moves for each key press
    FINISH_LINE_Y: int = 280 # Y coordinate where crossing finishes


    #---------- INITIALISATION ----------#

    def __init__(self) -> None:
        """Create player turtle at the starting position."""
        super().__init__()
        self.shape(self.SHAPE)
        self.penup()
        self.color(self.COLOUR)
        self.goto(self.STARTING_POSITION)
        self.setheading(90) # Point upwards
    

    #---------- PUBLIC METHODS ----------#

    def move(self) -> None:
        """Move the turtle upwards, stopping at the finish line."""
        new_y = self.ycor() + self.MOVE_DISTANCE
        if new_y < self.FINISH_LINE_Y: # Stop at finish line
            self.goto(self.xcor(), new_y)