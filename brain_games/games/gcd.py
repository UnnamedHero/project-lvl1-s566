from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def calculate_gcd(num1, num2):
    (a, b) = (num1, num2) if num1 >= num2 else (num2, num1)
    expected = a % b
    if expected == 0:
        return b
    else:
        return calculate_gcd(b, expected)


def get_question_data():
    number1 = randint(0, MAX_NUMBER)
    number2 = randint(0, MAX_NUMBER)
    question_text = "{} {}".format(number1, number2)
    correct_answer = str(calculate_gcd(number1, number2))
    return (question_text, correct_answer)
