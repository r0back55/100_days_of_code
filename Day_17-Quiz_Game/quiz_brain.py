# TODO: asking the question
# TODO: checking if the answer was right
# TODO: checking if we are at the end of the quiz


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Function returns False is code get to the last question on the list,
        else it keeps iterating through the list of questions"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Pulls up the question from the list depending on
        which current question number were on """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"That's wrong!")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
