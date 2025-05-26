class Question:
    """Represents a quiz question with its text and correct answer."""

    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer