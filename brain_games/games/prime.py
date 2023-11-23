from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    return d == number


def task_func():
    random_number = randint(1, 100)
    question = random_number
    if is_prime(random_number) is True:
        correct_answer = 'yes'
    elif is_prime(random_number) is False:
        correct_answer = 'no'
    return question, correct_answer
