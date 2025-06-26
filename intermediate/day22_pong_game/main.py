from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

#---------- CONSTANTS ----------#

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
PADDLE_X: int = 350
PADDLE_Y: int = 0
BALL_SPEED: float = 0.1    # Time delay in seconds


#---------- SETUP DISPLAY AND CONTROLS ----------#

def create_screen() -> Screen:
    """Initialise and return the main game screen."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0) # Turn off automatic animation
    screen.listen()
    return screen


def bind_keys(screen: Screen, paddle: Paddle, key_up: str, key_down: str) -> None:
    """Bind keyboard keys to paddle movement functions."""
    screen.onkeypress(key=key_up, fun=paddle.move_up)
    screen.onkeypress(key=key_down, fun=paddle.move_down)


#---------- GAME LOGIC ----------#


#---------- MAIN GAME LOOP ----------#

def start_game(screen:Screen) -> None:
    """Launch and manage the full game flow including replay loop."""
    right_paddle = Paddle(x=PADDLE_X, y=PADDLE_Y)
    left_paddle = Paddle(x=-PADDLE_X, y=PADDLE_Y)
    
    bind_keys(screen, right_paddle, key_up="Up", key_down="Down")
    bind_keys(screen, left_paddle, key_up="w", key_down="s")

    ball = Ball()
    screen.update()

    while True:
        time.sleep(BALL_SPEED)
        ball.move()
        screen.update()


# ---------- ENTRY POINT ---------- #

def main() -> None:
    screen = create_screen()
    start_game(screen)
    screen.mainloop()


if __name__ == "__main__":
    main()