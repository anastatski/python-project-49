import prompt


def run_game(get_question_and_answer, instruction):
    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(f'{instruction}')
    attempts = 3
    
    for _ in range(attempts):
        question, correct_answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!")
            return
            
    print(f'Congratulations, {name}!')