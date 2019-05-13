from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'
MIN_NUMBER = 2
MAX_NUMBER = 100


def is_prime(num):
    max_divider = num // 2
    current_divider = 2

    while current_divider <= max_divider:
        if not num % current_divider:
            return False
        current_divider += 1

    return True


def get_question_data():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return (str(number), correct_answer)
