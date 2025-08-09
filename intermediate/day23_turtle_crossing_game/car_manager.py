from turtle import Turtle
import random


class CarManager:
    """Manages cars for the Turtle Crossing game. Cars move leftwards."""

    #---------- CONSTANTS ----------#

    SHAPE: str = "square"
    COLOURS: list[str] = ["red", "orange", "yellow", "green", "blue", "purple"]
    HEIGHT: int = 1 # 1 * 20 = 20 high
    WIDTH: int = 2 # 2 * 20 = 40 wide
    STARTING_X: int = 280
    Y_RANGE: tuple[int, int] = [-240, 240]
    STARTING_MOVE_DISTANCE: int = 5

    #---------- INITIALISATION ----------#

    def __init__(self) -> None:
        """Initialise car manager with empty car list and base speed."""
        self.cars: list[Turtle] = []
        self.car_speed: int = self.STARTING_MOVE_DISTANCE


    #---------- PUBLIC METHODS ----------#

    def create_car(self) -> None:
        """Create a new car at a random y position on the right edge."""
        new_car = Turtle(shape=self.SHAPE)
        new_car.penup()
        new_car.shapesize(stretch_wid=self.HEIGHT, stretch_len=self.WIDTH)
        new_car.color(random.choice(self.COLOURS))
        new_car.goto(self.STARTING_X, random.randint(*self.Y_RANGE)) # * unpacks tuple
        new_car.setheading(180) # Face leftwards
        self.cars.append(new_car)
    

    def move_cars(self) -> None:
        """Move all cars leftwards by the current car speed."""
        for car in self.cars:
            car.forward(self.car_speed)