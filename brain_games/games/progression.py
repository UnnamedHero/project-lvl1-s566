from random import randint


DESCRIPTION = 'What number is missing in the progression?'
MAX_START_NUMBER = 20
PROGRESSION_LENGTH = 10
MAX_STEP = 10


def get_question_data():
    step = randint(1, MAX_STEP)
    start_num = randint(1, MAX_START_NUMBER)
    missing_index = randint(0, PROGRESSION_LENGTH - 1)
    end_num = (PROGRESSION_LENGTH * step) + start_num
    progression = [str(num) for num in range(start_num,
                                             end_num,
                                             step)]
    correct_answer = progression[missing_index]
    progression[missing_index] = '..'
    return (' '.join(progression), correct_answer)
