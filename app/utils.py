import os

SCORES_FILE_NAME = os.path.join(os.path.dirname(__file__), 'scores', 'scores.txt')
BAD_RETURN_CODE = "ERROR"


def screen_cleaner():
    os.system('clear')

