import os
import random
import time
import styles
import utils


def generate_sequence(difficulty):
    random_list = random.sample(range(1, 101), difficulty)
    styles.menu_items(f"The random list is: {random_list}")
    time.sleep(0.7)
    utils.screen_cleaner()
    return random_list


def get_list_from_user(difficulty):
    user_list = []
    while difficulty > 0:
        number = int(input(f"Enter your guess ({difficulty}): "))
        if 1 <= number <= 101:
            user_list.append(number)
            difficulty -= 1
        else:
            styles.error_message('Please enter the guesses (1-101): ')
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
        return True
    else:
        styles.error_message('Sorry you have not remembered them all! ')
        return False
