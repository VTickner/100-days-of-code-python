from turtle import Screen
from snake import Snake
import time


#---------- CONSTANTS ----------#

SCREEN_WIDTH: int = 600
SCREEN_HEIGHT: int = 600
SNAKE_SPEED: float = 0.1 # Time delay in seconds


#---------- SETUP DISPLAY AND CONTROLS ----------#

def create_screen() -> Screen:
    """Initialise and return the main game screen."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0) # Turns off automatic screen updates
    return screen


def bind_keys(screen:Screen, snake:Snake) -> None:
    """Bind keyboard keys to snake movement functions"""
    screen.listen()
    screen.onkeypress(key="Up", fun=snake.up)
    screen.onkeypress(key="Down", fun=snake.down)
    screen.onkeypress(key="Left", fun=snake.left)
    screen.onkeypress(key="Right", fun=snake.right)


#---------- MAIN PROGRAM ----------#

def main() -> None:
    """Run the main loop for the snake game."""
    screen = create_screen()
    snake = Snake()
    bind_keys(screen, snake)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(SNAKE_SPEED) # Adds a delay to make the snake's movement appear smooth and cohesive
        snake.move_snake()

    screen.exitonclick()


# ---------- ENTRY POINT ---------- #

if __name__ == "__main__":
    main()