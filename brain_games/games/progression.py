from random import randint, choice

RULES = 'What number is missing in the progression?'

def task_func():
    start_num = randint(1, 20)
    step = randint(1, 5)
    list_progression = [start_num + step * i for i in range(10)]
    correct_answer_int = choice(list_progression)
    correct_answer = str(correct_answer_int)
    modified_progression = ' '.join(str(num) if num != correct_answer_int else '..' for num in list_progression)
    question = modified_progression
    return question, correct_answer
