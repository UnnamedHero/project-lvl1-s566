from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'
MAX_NUMBER = 10
MAX_OPERATIONS = 3


def get_sign():
    return choice('+-*')


def get_calc_result(num1, num2, sign):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    else:
        return num1 * num2


def get_question_data():
    number1 = randint(0, MAX_NUMBER)
    number2 = randint(0, MAX_NUMBER)
    sign = get_sign()
    correct_answer = get_calc_result(number1, number2, sign)
    question = '{} {} {}'.format(number1, sign, number2)
    return (question, str(correct_answer))
