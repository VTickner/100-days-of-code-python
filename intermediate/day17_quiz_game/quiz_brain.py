class QuizBrain:
    """Controls the flow of the quiz, keeping track of questions, user input and score."""

    def __init__(self, question_list: list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = question_list


    def _check_answer(self, user_answer: str, correct_answer: str) -> None:
        """Check if the user answered the question correctly and keeps score of correct answers"""
        if user_answer.strip().lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")


    def _get_choice(self, prompt: str) -> str:
        """Prompt user for True/False answer, case-insensitive."""
        while True:
            choice = input(prompt).strip().lower()
            if choice in ["true", "false"]:
                return choice
            print("Invalid input. Please enter either True or False.")
        

    def has_more_questions(self) -> bool:
        """Check if there are more questions left in the quiz."""
        return self.question_number < len(self.question_list)

    
    def get_next_question(self) -> None:
        """Display the next question and prompts the user for a True/False answer."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = self._get_choice(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self._check_answer(user_answer, current_question.answer)