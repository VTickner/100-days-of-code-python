from turtle import Turtle

class Paddle(Turtle):
    """Paddle for the Pong game. Moves up and down."""

    #---------- CONSTANTS ----------#

    COLOUR: str = "white"
    SHAPE: str = "square"
    HEIGHT: int = 5 # 5 * 20 = 100 tall
    WIDTH: int = 1 # 1 * 20 = 20 wide
    MOVE_DISTANCE: int = 20 # Distance paddle moves for each key press


    #---------- INITIALISATION ----------#

    def __init__(self, x: int, y: int) -> None:
        """Create paddle at specified position."""
        super().__init__()
        self.shape(self.SHAPE)
        self.penup()
        self.shapesize(stretch_wid=self.HEIGHT, stretch_len=self.WIDTH)
        self.color(self.COLOUR)
        self.goto(x, y)


    #---------- PUBLIC METHODS ----------#

    def move_up(self) -> None:
        """Move the paddle up."""
        new_y = self.ycor() + self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    
    def move_down(self) -> None:
        """Move the paddle down."""
        new_y = self.ycor() - self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)