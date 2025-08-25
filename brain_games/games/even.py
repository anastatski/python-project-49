
import random

from brain_games.engine import run_game

EVEN_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):

    return number % 2 == 0
# функция-предикат: возвращает boolean значение!!!


def get_num_and_answer_if_even() -> tuple:
    
    random_number = random.randint(1, 100)
    answer = 'yes' if is_even(random_number) else 'no'

    return random_number, answer


def run_even_game():
    run_game(get_num_and_answer_if_even, EVEN_INSTRUCTION)
