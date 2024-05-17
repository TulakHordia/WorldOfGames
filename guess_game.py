import random
import styles


def generate_number(difficulty):
    secret_number = random.randint(0, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    guessed_number = input("Please enter a number between 0 and " + str(difficulty) + ": ")
    return guessed_number


def compare_results(secret_number, guessed_number):
    if secret_number == guessed_number:
        return True
    else:
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    guessed_number = get_guess_from_user(difficulty)
    if compare_results(secret_number, guessed_number):
        styles.choice_result("Congrats! You guessed the correct number!")
        return True
    else:
        styles.error_message("Sorry, you guessed the wrong number!")
        return False
