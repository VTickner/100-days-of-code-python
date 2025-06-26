from turtle import Turtle

class Ball(Turtle):
    """Ball for the Pong game."""

    #---------- CONSTANTS ----------#

    COLOUR: str = "white"
    SHAPE: str = "circle"
    HEIGHT: int = 1 # 1 * 20 = 20 tall
    WIDTH: int = 1 # 1 * 20 = 20 wide
    MOVE_DISTANCE: int = 10
    COLLISION_Y_LIMIT: int = 280
    START_HEADING: int = 45
    START_POS_X: int = 9
    START_POS_Y: int = 0


    #---------- INITIALISATION ----------#

    def __init__(self) -> None:
        super().__init__()
        self.shape(self.SHAPE)
        self.penup()
        self.shapesize(stretch_wid=self.HEIGHT, stretch_len=self.WIDTH)
        self.color(self.COLOUR)
        self.goto(x=self.START_POS_X, y=self.START_POS_Y)
        self.setheading(self.START_HEADING)


    #---------- PRIVATE METHODS ----------#

    def _wall_bounce(self) -> None:
        """Reverse vertical direction if hit top or bottom wall."""
        if abs(self.ycor()) > self.COLLISION_Y_LIMIT:
            self.setheading(-self.heading())


    #---------- PUBLIC METHODS ----------#

    def move(self) -> None:
        """Move the ball in its current direction and bounce off top/bottom walls if needed."""
        self.forward(self.MOVE_DISTANCE)
        self._wall_bounce()
