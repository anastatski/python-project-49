import random

from brain_games.engine import run_game

PRIME_INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    
    if number < 2:
        return False
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1
    return True


def get_num_and_answer_if_prime():
    random_number = random.randint(1, 15)
    if is_prime(random_number):
        answer = 'yes'
    else:
        answer = 'no'

    return random_number, answer


def run_prime_game():
    run_game(get_num_and_answer_if_prime, PRIME_INSTRUCTION)