import prompt

GAME_STEPS = 3


def run(game=None):
    print("Welcome to the Brain Games!")
    if game:
        print(game.DESCRIPTION)
        print()

    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print()

    if not game:
        return

    for step in range(0, GAME_STEPS):
        (question, correct_answer) = game.get_question_data()
        print('Question: {} '.format(question))
        answer = input('Your answer: ')
        if answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'"
                  .format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')
    print('Congratulation, {}!'.format(name))
