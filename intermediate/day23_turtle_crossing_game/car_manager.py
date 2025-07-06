from turtle import Turtle


class CarManager(Turtle):
    """Manages ars for the Turtle Crossing game. Cars move leftwards."""

    #---------- CONSTANTS ----------#

    COLORS: list[str] = ["red", "orange", "yellow", "green", "blue", "purple"]
    STARTING_MOVE_DISTANCE: int = 5
    MOVE_INCREMENT: int = 10

    pass
