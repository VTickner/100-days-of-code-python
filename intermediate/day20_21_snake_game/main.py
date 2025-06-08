from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


#---------- CONSTANTS ----------#

SCREEN_WIDTH: int = 600
SCREEN_HEIGHT: int = 600
SNAKE_SPEED: float = 0.5    # Time delay in seconds
FOOD_DISTANCE: int = 15     # Distance snake is away from food for it to hit it
WALL_LIMIT: int = 280       # Boundary for collision detection 
TAIL_COLLISION_DISTANCE: int = 10


#---------- SETUP DISPLAY AND CONTROLS ----------#

def create_screen() -> Screen:
    """Initialise and return the main game screen."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0) # Turns off automatic screen updates
    return screen


def bind_keys(screen: Screen, snake: Snake) -> None:
    """Bind keyboard keys to snake movement functions"""
    screen.listen()
    screen.onkeypress(key="Up", fun=snake.up)
    screen.onkeypress(key="Down", fun=snake.down)
    screen.onkeypress(key="Left", fun=snake.left)
    screen.onkeypress(key="Right", fun=snake.right)


#---------- GAME LOGIC ----------#

def check_food_collision(snake: Snake, food: Food, scoreboard: Scoreboard) -> None:
    """Check if the snake has eaten the food."""
    if snake.head.distance(food) < FOOD_DISTANCE:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()


def check_wall_collision(snake: Snake) -> bool:
    """Return True if the snake hits the wall."""
    x, y = snake.head.xcor(), snake.head.ycor()
    return x > WALL_LIMIT or x < -WALL_LIMIT or y > WALL_LIMIT or y < -WALL_LIMIT


def check_tail_collision(snake: Snake) -> bool:
    """Return True if the snake hits its own tail."""
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < TAIL_COLLISION_DISTANCE:
            return True
    return False


#---------- MAIN PROGRAM ----------#

def main() -> None:
    """Run the main loop for the snake game."""
    screen = create_screen()
    snake = Snake()
    bind_keys(screen, snake)
    food = Food()
    scoreboard = Scoreboard()

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(SNAKE_SPEED) # Adds a delay to make the snake's movement appear smooth and cohesive
        snake.move_snake()

        check_food_collision(snake, food, scoreboard)

        if check_wall_collision(snake) or check_tail_collision(snake):
            scoreboard.game_over()
            game_is_on = False
            break

    screen.exitonclick()


# ---------- ENTRY POINT ---------- #

if __name__ == "__main__":
    main()