from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no"'
MAX_NUMBER = 100


def get_question_data():
    number = randint(0, MAX_NUMBER)
    correct_answer = 'yes' if number % 2 == 1 else 'no'
    return (str(number), correct_answer)
