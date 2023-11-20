from random import randint, choice

RULES = 'What number is missing in the progression?'


def progression():
    start_num = randint(1, 20)
    step = randint(1, 5)
    list_progression = [start_num + step * i for i in range(10)]
    return list_progression


def question_string():
    progression_variable = progression()
    missing_element_int = choice(progression_variable)
    missing_element = str(missing_element_int)
    modified_progression = ''
    for num in progression_variable:
        if num != missing_element_int:
            modified_progression = modified_progression + str(num) + ' '
        else:
            modified_progression += '.. '
    return modified_progression, missing_element


def task_func():
    modified_progression, missing_element = question_string()
    question = modified_progression
    correct_answer = missing_element
    return question, correct_answer
