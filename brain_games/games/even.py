from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def task_func():
    random_number = randint(MIN_NUM, MAX_NUM)
    question = random_number
    correct_answer = 'yes' if is_even(random_number) is True else 'no'
    return question, correct_answer
