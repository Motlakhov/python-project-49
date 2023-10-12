#!/usr/bin/env python3

import prompt
from random import randint

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'Answer "yes" if the number is even, otherwise answer "no"')
    score = 0
    finish = 3
    while score < finish:
        random_number = randint(1,100)
        print(f'Question:{random_number}')
        user_answer = prompt.string('Your answer: ') 
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        if user_answer == correct_answer:
            print('Correct!')
            score += 1
        elif user_answer != correct_answer:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet's try again, {name}!")
            break
        if score == finish:
            print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
