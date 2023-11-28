from random import randint, choice

RULES = 'What number is missing in the progression?'
MIN_START_NUM = 1
MAX_START_NUM = 20
MIN_STEP = 2
MAX_STEP = 10


def calculate_progression(start_num, step, num_terms):
    progression = [start_num + step * i for i in range(num_terms)]
    return progression


def question_string(progression):
    missing_element_int = choice(progression)
    missing_element = str(missing_element_int)
    modified_progression = ''
    for num in progression:
        if num != missing_element_int:
            modified_progression = modified_progression + str(num) + ' '
        else:
            modified_progression += '.. '
    return modified_progression, str(missing_element)


def task_func():
    start_num = randint(MIN_START_NUM, MAX_START_NUM)
    step = randint(MIN_STEP, MAX_STEP)
    num_terms = 10
    progression_result = calculate_progression(start_num, step, num_terms)
    question, correct_answer = question_string(progression_result)
    return question, correct_answer
