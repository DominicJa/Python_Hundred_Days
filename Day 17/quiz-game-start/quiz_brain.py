class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return 1
        else:
            return 0

    def next_question(self):
        current_q_number = self.question_number
        current_q_text = self.question_list[current_q_number].text
        current_q_answer = self.question_list[current_q_number].answer
        user_answer = input(f"Q.{current_q_number + 1}: {current_q_text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(user_answer, current_q_answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {c_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
