from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def task_func():
    random_number = randint(1, 100)
    question = random_number
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                     43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for number in prime_numbers:
        if number == random_number:
            correct_answer = 'yes'
            break
        else:
            correct_answer = 'no'
    return question, correct_answer
