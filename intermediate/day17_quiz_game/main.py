from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def run_quiz():
    """Initialise and run the quiz loop."""
    question_bank = [Question(question["text"], question["answer"]) for question in question_data]
    quiz = QuizBrain(question_bank)

    while quiz.has_more_questions():
        quiz.get_next_question()

    print("You've completed the quiz.")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}.")


if __name__ == "__main__":
    run_quiz()