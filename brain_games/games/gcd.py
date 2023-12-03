from random import randint
from math import gcd

RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUM = 1
MAX_NUM = 100


def task_func():
    num1 = randint(MIN_NUM, MAX_NUM)
    num2 = randint(MIN_NUM, MAX_NUM)
    question = (f'{num1} {num2}')
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
