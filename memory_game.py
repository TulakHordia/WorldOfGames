import random
import styles


def generate_sequence(difficulty):
    random_list = random.sample(range(1, 101), len(difficulty))
    return random_list


def get_list_from_user(difficulty):
    user_list = []
    while difficulty > 0:
        number = int(input('Enter a number between 1 and 101: '))
        if 1 <= number <= 101:
            user_list.append(number)
            difficulty -= 1
        else:
            styles.error_message('Please enter a number between 1 and 101. ')
    return user_list


def is_list_equal(auto_generated_list, user_generated_list):
    if auto_generated_list == user_generated_list:
        return True
    else:
        return False


def play(difficulty):
    random_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    if is_list_equal(random_list, user_list):
        styles.choice_result('Congratulations! you remembered them all! ')
    else:
        styles.error_message('Sorry you have not remembered them all! ')