from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def is_even(number):
    return number % 2 == 0


def get_question_and_correct_answer():
    random_number = randint(MIN_NUM, MAX_NUM)
    question = random_number
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return question, correct_answer
