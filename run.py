from trivia import sport_questions
# LOGO


#Question class
class Question:
    """
    Create and initialise objects for the questions class.
    """

    def __init__(self, question, correct_answer):
        self.question = question
        self.answer = correct_answer


# first_question = Question("What's your name?", "True")
# print(first_question.question)


# 2. For loop to go over the  the list of trivia questions in the database
array_of_questions = []
"""
The for loop will go over the questions in the database in trivia.py. For each question an object will be created and appended to the array of questions.
"""
for sport_questions
