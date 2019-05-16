from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def calculate_gcd(num1, num2):    
    expected = num1 % num2
    if expected == 0:
        return num2
    else:
        return calculate_gcd(num2, expected)


def get_question_data():
    number1 = randint(0, MAX_NUMBER)
    number2 = randint(0, MAX_NUMBER)
    question_text = "{} {}".format(number1, number2)
    correct_answer = str(calculate_gcd(number1, number2))
    return (question_text, correct_answer)
