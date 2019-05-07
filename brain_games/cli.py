import prompt


def run():
    print("Welcome to the Brain Games!", end='\n\n')
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
