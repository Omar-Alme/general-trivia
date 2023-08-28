# LOGO


# Question class
class Question:
    """
    Create and initialise objects for the questions class
    """

    def __init__(self, question, correct_answer):
        self.question = question
        self.answer = correct_answer


first_question = Question("What's your name?", "True")
print(first_question.question)
