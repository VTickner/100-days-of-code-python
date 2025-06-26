from turtle import Turtle
from paddle import Paddle

class Ball(Turtle):
    """Ball object for Pong game that moves, bounces off walls/paddles, and resets when missed."""

    #---------- CONSTANTS ----------#

    COLOUR: str = "white"
    SHAPE: str = "circle"
    HEIGHT: int = 1 # 1 * 20 = 20 tall
    WIDTH: int = 1 # 1 * 20 = 20 wide
    START_HEADING: int = 45
    START_POS_X: int = 9
    START_POS_Y: int = 0
    MOVE_DISTANCE: int = 10
    COLLISION_Y_LIMIT: int = 280
    SCREEN_X_LIMIT: int = 380
    HIT_RANGE: int = 50


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

    def _bounce_x(self) -> None:
        """Reverse the ball's horizontal direction."""
        self.setheading(180 - self.heading())


    def _bounce_y(self) -> None:
        """Reverse vertical direction if hit top or bottom wall."""
        if abs(self.ycor()) > self.COLLISION_Y_LIMIT:
            self.setheading(-self.heading())


    #---------- PUBLIC METHODS ----------#

    def move(self) -> None:
        """Move the ball in its current direction and apply vertical wall bounce logic.."""
        self.forward(self.MOVE_DISTANCE)
        self._bounce_y()
    

    def paddle_collision(self, paddle: Paddle, x_threshold: int) -> None:
        """Bounce off paddle if within distance and past x-threshold."""
        if self.distance(paddle) < self.HIT_RANGE and abs(self.xcor()) > abs(x_threshold):
            self._bounce_x()


    def reset_if_missed(self) -> None:
        """Reset ball to centre and reverse horizontal direction if ball goes past left or right edge of screen."""
        if abs(self.xcor()) > self.SCREEN_X_LIMIT:
            self.goto(x=self.START_POS_X, y=self.START_POS_Y)
            self._bounce_x()