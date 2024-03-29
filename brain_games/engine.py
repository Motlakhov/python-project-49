import prompt

ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    win_score = 0
    while win_score < ROUNDS:
        question, correct_answer = game.get_question_and_correct_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            win_score += 1
        elif answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
        if win_score == ROUNDS:
            print(f'Congratulations, {name}!')
