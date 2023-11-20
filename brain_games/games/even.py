from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def task_func():
    random_number = randint(1, 100)
    question = random_number
    correct_answer = 'yes' if is_even(random_number) == True else 'no'
    return question, correct_answer
