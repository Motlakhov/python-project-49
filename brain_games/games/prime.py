from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number


def task_func():
    random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = random_number
    if is_prime(random_number) is True:
        correct_answer = 'yes'
    elif is_prime(random_number) is False:
        correct_answer = 'no'
    return question, correct_answer
