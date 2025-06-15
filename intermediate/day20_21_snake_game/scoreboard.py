from turtle import Turtle
import os

class Scoreboard(Turtle):
    """Handles score display and updates during the Snake game."""

    #---------- CONSTANTS ----------#

    COLOUR: str = "white"
    ALIGNMENT: str = "center"
    FONT: tuple[str, int, str] = ("Courier", 16, "bold")
    SCORE_X: int = 0
    SCORE_Y: int = 260
    BASE_DIR: str = os.path.dirname(__file__) # Folder of this script
    FILE_PATH: str = os.path.join(BASE_DIR, "high_score.txt")
    

    #---------- INITIALISATION ----------#

    def __init__(self) -> None:
        super().__init__()
        self.score: int = 0
        self.high_score = self._read_high_score()
        self.hideturtle()
        self.penup()
        self.color(self.COLOUR) # Ensures text is visible on black background
        self.goto(x=self.SCORE_X, y=self.SCORE_Y)
        self.display_score()
    

    #---------- PRIVATE METHODS ----------#

    def _read_high_score(self) -> int:
        """Read the high score from the file."""
        try:
            with open(self.FILE_PATH, "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0
    

    def _save_high_score(self) -> None:
        """Write the high score to the file."""
        with open(self.FILE_PATH, "w") as file:
            file.write(str(self.high_score))


    #---------- PUBLIC METHODS ----------#

    def display_score(self) -> None:
        """Display the current score and high score."""
        self.clear()
        self.write(arg=f"Score: {self.score}          High Score: {self.high_score}", align=self.ALIGNMENT, font=self.FONT)


    def increase_score(self) -> None:
        """Increase score by 1 and update display."""
        self.score += 1
        self.display_score()
    

    def reset(self) -> None:
        """Reset score and display high score if needed."""
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()
        self.score = 0
        self.display_score()
    

    def game_over(self) -> None:
        """Display 'Game Over' message at the screen centre."""
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=self.ALIGNMENT, font=self.FONT)