from turtle import Turtle
import random

class Food(Turtle):
    """Food for the Snake game. Appears randomly and detects when eaten."""

    #---------- CONSTANTS ----------#

    SHAPE: str = "circle"
    SIZE: float = 0.5 # Half the size
    COLOUR: str = "blue"
    SPEED: str = "fastest"
    MIN_POS: int = -280
    MAX_POS: int = 280


    #---------- INITIALISATION ----------#

    def __init__(self) -> None:
        super().__init__()
        self.shape(self.SHAPE)
        self.penup()
        self.shapesize(stretch_len=self.SIZE, stretch_wid=self.SIZE)
        self.color(self.COLOUR)
        self.speed(self.SPEED)
        self.refresh()


    #---------- PUBLIC METHODS ----------#

    def refresh(self) -> None:
        """Reposition the food to a random location within the screen limits."""
        x = random.randint(self.MIN_POS, self.MAX_POS) 
        y = random.randint(self.MIN_POS, self.MAX_POS)
        self.goto(x, y)