from random import randint, choice

RULES = 'What number is missing in the progression?'


def progression(start_num, step, num_terms):
    list_progression = [start_num + step * i for i in range(num_terms)]
    return list_progression


def question_string(progression):
    missing_element_int = choice(progression)
    missing_element = str(missing_element_int)
    modified_progression = ''
    for num in progression:
        if num != missing_element_int:
            modified_progression = modified_progression + str(num) + ' '
        else:
            modified_progression += '.. '
    return modified_progression, missing_element


def task_func():
    list_progression = progression(randint(1, 20), randint(1, 5), 10)
    modified_progression, missing_element = question_string(list_progression)
    question = modified_progression
    correct_answer = missing_element
    return question, correct_answer
