from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

#---------- CONSTANTS ----------#

SCREEN_WIDTH: int = 600
SCREEN_HEIGHT: int = 600

#---------- SETUP DISPLAY ----------#


def create_screen() -> Screen:
    """Initialise and return the main game screen."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Turtle Crossing Game")
    screen.tracer(0) # Turn off automatic animation
    screen.listen()
    return screen


#---------- MAIN GAME LOOP ----------#

def start_game(screen:Screen) -> None:
    """Launch and manage the full game flow including replay loop."""
    turtle = Player()
    screen.onkeypress(key="Up", fun=turtle.move)

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()


# ---------- ENTRY POINT ---------- #

def main() -> None:
    """Entry point for the game. Sets up the screen and starts game logic."""
    screen = create_screen()
    start_game(screen)
    screen.mainloop()


if __name__ == "__main__":
    main()
