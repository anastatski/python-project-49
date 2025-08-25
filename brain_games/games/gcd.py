import math
import random

from brain_games.engine import run_game

GCD_INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def get_nums_pair_and_gcd():
    
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    nums_pair = f'{num1} {num2}'
    gcd = math.gcd(num1, num2)
    
    return nums_pair, str(gcd)


def run_gcd_game():
    run_game(get_nums_pair_and_gcd, GCD_INSTRUCTION)