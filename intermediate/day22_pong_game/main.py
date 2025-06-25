from turtle import Screen
from paddle import Paddle

#---------- CONSTANTS ----------#

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
PADDLE_X: int = 350
PADDLE_Y: int = 0


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
    right_paddle = Paddle(PADDLE_X, PADDLE_Y)
    left_paddle = Paddle(-PADDLE_X, PADDLE_Y)
    bind_keys(screen, right_paddle, "Up", "Down")
    bind_keys(screen, left_paddle, "w", "s")
    screen.update()

    while True:
        screen.update()


# ---------- ENTRY POINT ---------- #

def main() -> None:
    screen = create_screen()
    start_game(screen)
    screen.mainloop()


if __name__ == "__main__":
    main()