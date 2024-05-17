import utils


def add_score(difficulty):
    filename = utils.SCORES_FILE_NAME
    POINTS_OF_WINNING = (difficulty*3)+5

    try:
        with open(filename, 'r') as file:
            content = file.read()
            if content.isdigit():
                current_score = int(content)
            else:
                current_score = 0
    except FileNotFoundError:
        print(f"File not found, creating a new scores.txt")
        current_score = 0
    new_score = current_score + POINTS_OF_WINNING
    with open(filename, 'w') as file:
        file.write(str(new_score))

    print(f"The new score is: {new_score}")

