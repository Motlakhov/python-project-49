from operator import add, sub, mul
from random import choice, randint

RULES = 'What is the result of the expression?'

def task_func():
    num1 = randint(10, 30)
    num2 = randint(1, 20)
    operations = ((add, '+'), (sub, '-'), (mul, '*'))
    random_operator, sign = choice(operations)
    question = (f'{num1} {sign} {num2}')
    correct_answer = str(random_operator(num1, num2))
    return question, correct_answer
