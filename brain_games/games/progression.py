import random

from brain_games.engine import run_game

PROGRESSION_INSTRUCTION = 'What number is missing in the progression?'


def get_progr_and_missing_num():
    start = random.randint(1, 50)
    step = random.randint(2, 10)
    progr = []
    progr_length = random.randint(5, 10)
    for i in range(progr_length):
        progr.append(start + step * i)

    missed_index = random.randint(0, progr_length - 1)
    missed_num = progr[missed_index]
    progr[missed_index] = '..'
    progr_with_missed_num = ' '.join(map(str, progr))

    return progr_with_missed_num, str(missed_num)


def run_progression_game():
    run_game(get_progr_and_missing_num, PROGRESSION_INSTRUCTION)