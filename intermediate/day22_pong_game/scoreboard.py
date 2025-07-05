from turtle import Turtle

class Scoreboard(Turtle):
    """Scoreboard for the Pong game, keeps track and displays player scores."""

    #---------- CONSTANTS ----------#

    COLOUR: str = "white"
    FONT: tuple = ("Courier", 60, "bold")
    ALIGN: str = "center"
    SCREEN_X_LIMIT: int = 380


    #---------- INITIALISATION ----------#

    def __init__(self, x: int, y: int) -> None:
        """Create scoreboard at specified position."""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(self.COLOUR)
        self.left_score = 0
        self.right_score = 0
        self.left_score_pos = (x, y)
        self.right_score_pos = (-x, y)
        self._update_scoreboard()
    

    #---------- PRIVATE METHODS ----------#

    def _update_scoreboard(self) -> None:
        """Clear previous scores and redraw the current scores."""
        self.clear()
        self.goto(self.left_score_pos)
        self.write(self.left_score, align=self.ALIGN, font=self.FONT)
        self.goto(self.right_score_pos)
        self.write(self.right_score, align=self.ALIGN, font=self.FONT)


    #---------- PUBLIC METHODS ----------#

    def point(self, paddle_missed: str) -> None:
        """Increment point score depending on which paddle missed."""
        if paddle_missed == "right":
            self.left_score += 1
        elif paddle_missed == "left":
            self.right_score += 1
        self._update_scoreboard()