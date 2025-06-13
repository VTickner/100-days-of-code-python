from turtle import Turtle, Screen

class Instructions(Turtle):
    """Handles displaying and clearing the game instructions."""

    #---------- CONSTANTS ----------#

    COLOUR: str = "white"
    ALIGNMENT: str = "center"
    FONT_NAME: str = "Courier"


    #---------- INITIALISATION ----------#

    def __init__(self, screen:Screen):
        super().__init__()
        self.screen = screen
        self.hideturtle()
        self.penup()
        self.color(self.COLOUR) # Ensures text is visible on black background


    #---------- PUBLIC METHODS ----------#

    def show(self) -> None:
        """Display the game instructions."""
        instructions = [
            ("Welcome to Snake Game!", 100, 16, "bold"),
            ("Controls:", 60, 12, "normal"),
            ("⬆️ - Move up | ⬇️ - Move down", 30, 10, "normal"),
            ("➡️ - Move right | ⬅️ - Move left", 10, 10, "normal"),
            ("Press any letter key to start...", -70, 10, "italic"),  
        ]
        
        for text, y, size, style in instructions:
            self.goto(0, y)
            self.write(arg=text, align=self.ALIGNMENT, font=(self.FONT_NAME, size, style))


    def wait_for_keypress(self, start_callback) -> None:
        """Wait for any key press, then clear instructions and start the game."""
        def _on_key_press():
            self.clear()
            self.screen.onkeypress(None) # Remove the generic key binding
            start_callback()

        self.screen.listen()
        self.screen.onkeypress(_on_key_press)