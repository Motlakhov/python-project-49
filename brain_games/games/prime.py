from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number


def get_question_and_correct_answer():
    random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = random_number
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
