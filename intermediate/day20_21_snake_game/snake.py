from turtle import Turtle

class Snake:
    """Represents the snake in a classic Snake game. Manages creation, movement and direction."""

    #---------- CONSTANTS ----------#

    COLOUR: str = "white"
    SHAPE: str = "square"
    STARTING_POSITIONS: list[tuple[int, int]] = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE: int = 20 # Distance each segment moves per step (size of each Turtle segment)
    UP: int = 90
    DOWN: int = 270
    LEFT: int = 180
    RIGHT: int = 0


    #---------- INITIALISATION ----------#

    def __init__(self) -> None:
        self.segments: list[Turtle] = []
        self._create_snake()
        self.head: Turtle = self.segments[0]
    

    #---------- PRIVATE METHODS ----------#

    def _create_snake(self) -> None:
        """Initialise the snake with starting segments."""
        for x, y in self.STARTING_POSITIONS:
            self._add_segment(x, y) 


    def _add_segment(self, x: int, y: int) -> None:
        """Add a new segment at the specified position."""
        segment = Turtle(shape=self.SHAPE)
        segment.color(self.COLOUR)
        segment.penup()
        segment.goto(x, y)
        self.segments.append(segment)


    #---------- PUBLIC METHODS ----------#

    def extend_snake(self) -> None:
        """Extend the snake by adding a new segment at the tail."""
        last = self.segments[-1]
        self._add_segment(last.xcor(), last.ycor())     


    def move_snake(self) -> None:
        """Move the snake forward, segment by segment."""
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(self.MOVE_DISTANCE)


    def up(self) -> None:
        """Turn upwards unless moving down."""
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)   


    def down(self) -> None:
        """Turn downwards unless moving up."""
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)
    

    def left(self) -> None:
        """Turn left unless moving right."""
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)


    def right(self) -> None:
        """Turn right unless moving left."""
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)