from turtle import Turtle

class Snake:
    """Represents the snake in a classic Snake game. Manages creation, movement and directional control of the snake segments."""

    #---------- CONSTANTS ----------#

    SNAKE_COLOUR: str = "white"
    SNAKE_SHAPE: str = "square"
    STARTING_POSITIONS: list[tuple[int, int]] = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE: int = 20 # Distance each segment moves per step (size of each Turtle segment)
    UP: int = 90
    DOWN: int = 270
    LEFT: int = 180
    RIGHT: int = 0


    #---------- INTERNAL METHODS ----------#

    def __init__(self) -> None:
        self.snake: list[Turtle] = self._create_snake()
        self.head: Turtle = self.snake[0]
    

    def _create_snake(self) -> list[Turtle]:
        """Create snake segments at the starting positions and store them in a list."""
        snake: list[Turtle] = []
        for x, y in self.STARTING_POSITIONS:
            segment = Turtle(shape=self.SNAKE_SHAPE)
            segment.color(self.SNAKE_COLOUR)
            segment.penup()
            segment.goto(x=x, y=y)
            snake.append(segment)
        return snake


    #---------- EXTERNAL METHODS ----------#

    def move_snake(self) -> None:
        """Move each segment to the position of the segment in front, then move the head forward."""
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(x=new_x, y=new_y)
        self.head.forward(self.MOVE_DISTANCE)


    def up(self) -> None:
        """Change direction to up unless currently moving down."""
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)   


    def down(self) -> None:
        """Change direction to down unless currently moving up."""
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)
    

    def left(self) -> None:
        """Change direction to left unless currently moving right."""
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)


    def right(self) -> None:
        """Change direction to right unless currently moving left."""
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)