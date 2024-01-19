from random import randint, choice

RULES = 'What number is missing in the progression?'
MIN_START_NUM = 1
MAX_START_NUM = 20
MIN_STEP = 2
MAX_STEP = 10
NUM_TERMS = 10


def calculate_progression(initial_term, common_difference, num_terms):
    progression = [initial_term + common_difference * i
                   for i in range(num_terms)]
    return progression


def question_string(progression, missing_index):
    modified_progression = []
    for i, num in enumerate(progression):
        if i != missing_index:
            modified_progression.append(str(num))
        else:
            modified_progression.append('..')
    modified_progression = ' '.join(modified_progression)
    return modified_progression, progression[missing_index]


def get_question_and_correct_answer():
    initial_term = randint(MIN_START_NUM, MAX_START_NUM)
    common_difference = randint(MIN_STEP, MAX_STEP)
    num_terms = NUM_TERMS
    progression_result = calculate_progression(initial_term,
                                               common_difference,
                                               num_terms)
    missing_index = choice(range(len(progression_result)))
    question, correct_answer = question_string(progression_result,
                                               missing_index)
    return question, str(correct_answer)
