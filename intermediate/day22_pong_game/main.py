from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#---------- CONSTANTS ----------#

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
PADDLE_X: int = 350
PADDLE_Y: int = 0
SCORE_X_POS: int = -100
SCORE_Y_POS: int = 200


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


#---------- MAIN GAME LOOP ----------#

def start_game(screen:Screen) -> None:
    """Launch and manage the full game flow including replay loop."""
    right_paddle = Paddle(x=PADDLE_X, y=PADDLE_Y)
    left_paddle = Paddle(x=-PADDLE_X, y=PADDLE_Y)

    bind_keys(screen=screen, paddle=right_paddle, key_up="Up", key_down="Down")
    bind_keys(screen=screen, paddle=left_paddle, key_up="w", key_down="s")

    ball = Ball()
    scoreboard = Scoreboard(x=SCORE_X_POS, y=SCORE_Y_POS)

    screen.update()

    while True:
        time.sleep(ball.speed)
        ball.move()
        
        # Detect collision with either paddle
        ball.paddle_collision(paddle=right_paddle, x_threshold=320)
        ball.paddle_collision(paddle=left_paddle, x_threshold=-320)

        # Detect paddle missed
        missed_paddle = ball.reset_if_missed()
        if missed_paddle:
            scoreboard.point(paddle_missed=missed_paddle)

        screen.update()


# ---------- ENTRY POINT ---------- #

def main() -> None:
    """Entry point for the game. Sets up the screen and starts game logic."""
    screen = create_screen()
    start_game(screen)
    screen.mainloop()


if __name__ == "__main__":
    main()