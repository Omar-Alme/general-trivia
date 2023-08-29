from trivia import general_questions
from logo import logo


class Question:
    """
    Create and initialise objects for the questions class.
    """

    def __init__(self, the_question, correct_answer):
        self.question = the_question
        self.answer = correct_answer


class TriviaFunction:
    def __init__(self, list):
        self.number_of_question = 0
        self.list_of_questions = list
        self.score = 0

    def next_question(self):
        """
        Retrieves question number from the list. Inputs the question and asks user for the answer.
        """
        current_q = self.list_of_questions[self.number_of_question]
        self.number_of_question += 1
        users_input = input(
            f"Question {self.number_of_question}: {current_q.question}(Select letter):  "
        )
        print("\n")
        self.answer_check(users_input, current_q.answer)

    def is_questions_remaining(self):
        """
        Checks if there are still remaining questions in the trivia. Keeps checking until all the questions have been printed.
        """
        if self.number_of_question < len(self.list_of_questions):
            return True
        else:
            False

    def answer_check(self, users_input, correct_answer):
        """
        Checks user input and compares it to correct answer from the object. If correct show correct answer text. If incorrect show incorrect answer as well as show what the correct answer is.
        """
        if users_input.lower() == correct_answer.lower():
            print("CORRECT ANSWER!")
            self.score += 1
        else:
            print("WRONG ANSWER. Better luck next time.")
            print(f"The correct answer is: {correct_answer}.")
        print(f"Your total score is {self.score} out of {self.number_of_question}")
        print("\n")


print(logo)

array_of_questions = []
"""
The for loop will go over the questions in the database in trivia.py. For each question an object will be created and appended to the array of questions.
"""
# i = 0
for question in general_questions:
    question_1 = question["question"]
    question_correct_answer = question["correct_answer"]
    # i += 1
    add_question = Question(question_1, question_correct_answer)
    array_of_questions.append(add_question)


trivia = TriviaFunction(array_of_questions)

while trivia.is_questions_remaining():
    trivia.next_question()

print("Well Done on finishing Sports Trivia!")
print("\n")
print(f"Your final score is {trivia.score}/{len(array_of_questions)}")
print("\n")
