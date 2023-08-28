from trivia import sport_questions


# Question class
class Question:
    """
    Create and initialise objects for the questions class.
    """

    def __init__(self, the_question, correct_answer):
        self.question = the_question
        self.answer = correct_answer


# first_question = Question("What's your name?", "True")
# print(first_question.question)


# 2. For loop to go over the  the list of trivia questions in the database
array_of_questions = []
"""
The for loop will go over the questions in the database in trivia.py. For each question an object will be created and appended to the array of questions.
"""
for question in sport_questions:
    question_1 = question[0]["question"]
    question_correct_answer = question[0]["correct_answer"]
    add_question = Question(question_1, question_correct_answer)
    array_of_questions.append(add_question)

print(array_of_questions)


# 3. Class that prints and runs the questions
class TriviaFunction:
    """
    Retrieves question number from the list. Inputs the question and asks user for the answer.
    """

    def __init__(self, list):
        self.number_of_question = 0
        self.list_of_questions = list
