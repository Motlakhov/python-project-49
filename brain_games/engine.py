import prompt

ROUNDS = 3

def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    win_score = 0
    while win_score < ROUNDS:
        correct_answer, question = game.task_func()
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            win_score += 1
        elif answer != correct_answer:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet's try again, {name}!")
        if win_score == finish:
            print(f'Congratulations, {name}!')
