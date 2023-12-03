from operator import add, sub, mul
from random import choice, randint

RULES = 'What is the result of the expression?'
MIN_NUM = 1
MAX_NUM = 100


def task_func():
    num1 = randint(MIN_NUM, MAX_NUM)
    num2 = randint(MIN_NUM, MAX_NUM)
    operations = ((add, '+'), (sub, '-'), (mul, '*'))
    random_operator, sign = choice(operations)
    question = (f'{num1} {sign} {num2}')
    correct_answer = str(random_operator(num1, num2))
    return question, correct_answer
