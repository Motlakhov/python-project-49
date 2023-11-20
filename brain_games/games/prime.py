from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                     43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if number in prime_numbers:
        return True
    elif number not in prime_numbers:
        return False


def task_func():
    random_number = randint(1, 100)
    question = random_number
    if is_prime(random_number) == True:
        correct_answer = 'yes'
    elif is_prime(random_number) == False:
        correct_answer = 'no'
    return question, correct_answer
