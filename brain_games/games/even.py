from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def task_func():
    random_number = randint(1, 100)
    question = random_number
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return question, correct_answer
