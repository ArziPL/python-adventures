from random import choice
from data import question_data

excluded_questions = []


# question -> generate random question and print it, return correct incorrect
# quiz -> create question, get correct/incorrect, add score, finish

class Question:
    def __init__(self):
        self.random_question_index = choice([i for i in range(len(question_data)) if i not in excluded_questions])
        self.question = question_data[self.random_question_index]
        excluded_questions.append(self.random_question_index)

    def ask_question(self):
        answer = input(f"{self.question['text']} => Write true or false: ").lower()
        if answer == self.question["answer"].lower():
            return True
        else:
            return False


class Quiz:
    def __init__(self):
        self.score = 0
        self.amount_of_questions = 5

    def play_round(self):
        new_question = Question()
        result = new_question.ask_question()
        if result is True:
            self.score += 1
        self.amount_of_questions -= 1
        print(f"{self.amount_of_questions} questions to end the game, answer was {new_question.question['answer']}\n")

    def game(self,amount_of_questions):
        self.amount_of_questions = amount_of_questions
        while self.amount_of_questions != 0:
            self.play_round()
        print(f"The game is over, your score is: {self.score}")
