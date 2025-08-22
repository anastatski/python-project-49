import operator
import random

from brain_games.engine import run_game

CALC_INSTRUCTION = 'What is the result of the expression?'


def get_expression_and_result():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operations = ['*', '+', '-']
    operation = random.choice(operations)
    expression = f'{number1} {operation} {number2}'

    if operation == '+':
        result = operator.add(number1, number2)
    elif operation == '-':
        result = operator.sub(number1, number2)
    elif operation == '*':
        result = operator.mul(number1, number2)
        
    return expression, str(result)


def run_calc_game():
    run_game(get_expression_and_result, CALC_INSTRUCTION)
# некая абстракция, поддержка скриптовых файлов в чистоте. Ничего лишнего