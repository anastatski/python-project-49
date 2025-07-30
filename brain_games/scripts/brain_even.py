import random

def main():
    print("Welcome to the Brain Games!")    
    user_name = input('May I have your name? ')
    print(f'Hello, {user_name}!')

    attempts = 3
    print('Answer "yes" if the number is even, otherwise answer "no"')
    
    for attempt in range(attempts):
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = input('Your answer is: ')
        
        if random_number % 2 == 0:
            if user_answer == 'yes':
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {user_name}!")
                break
        elif random_number % 2 != 0:
            if user_answer == 'no':
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'no'. Let's try again, {user_name}!")
                break

    print(f'Congratulations, {user_name}!')

if __name__ == "__main__":
    main()