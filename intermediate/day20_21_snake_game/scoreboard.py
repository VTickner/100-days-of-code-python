from turtle import Turtle

class Scoreboard(Turtle):
    """Handles score display and updates during the Snake game."""

    #---------- CONSTANTS ----------#

    COLOUR: str = "white"
    ALIGNMENT: str = "center"
    FONT: tuple[str, int, str] = ("Courier", 16, "bold")
    SCORE_X: int = 0
    SCORE_Y: int = 260
    

    #---------- INITIALISATION ----------#

    def __init__(self) -> None:
        super().__init__()
        self.score: int = 0
        self.hideturtle()
        self.penup()
        self.color(self.COLOUR) # Ensures text is visible on black background
        self.goto(x=self.SCORE_X, y=self.SCORE_Y)
    

    #---------- PUBLIC METHODS ----------#

    def display_score(self) -> None:
        """Display the current score."""
        self.write(arg=f"Score: {self.score}", align=self.ALIGNMENT, font=self.FONT)


    def increase_score(self) -> None:
        """Increase score by 1 and update display."""
        self.score += 1
        self.clear()
        self.display_score()
    

    def game_over(self) -> None:
        """Display 'Game Over' message at the screen centre."""
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=self.ALIGNMENT, font=self.FONT)