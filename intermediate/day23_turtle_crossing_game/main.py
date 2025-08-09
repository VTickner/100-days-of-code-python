from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

#---------- CONSTANTS ----------#

SCREEN_WIDTH: int = 600
SCREEN_HEIGHT: int = 600
CAR_FREQUENCY: int = 6 # Loops between new car spawns
FRAME_DELAY: float = 0.1 # Delay between game loop frames (seconds)


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
    """Launch and manage the full game flow including player, cars and levels."""
    player = Player()
    car_manager = CarManager()

    screen.onkeypress(key="Up", fun=player.move)

    i = 0
    game_is_on = True

    while game_is_on:
        time.sleep(FRAME_DELAY)
        screen.update()

        i += 1
        if i % CAR_FREQUENCY == 0:
            car_manager.create_car()
        
        car_manager.move_cars()

        # TODO: Add collision detection
        # TODO: Add level advancement
        # TODO: Add game over handling and replay option


# ---------- ENTRY POINT ---------- #

def main() -> None:
    """Entry point for the game. Sets up the screen and starts game."""
    screen = create_screen()
    start_game(screen)
    screen.mainloop()


if __name__ == "__main__":
    main()
