import guess_game
import memory_game
import currency_roulette_game
import styles
import score

error_message_1_to_5 = "Invalid input, Difficulty must be between 1 and 5"
error_message_1_to_3 = "Invalid input, Difficulty must be between 1 and 3"
invalid_input = "Invalid input. Please enter a number."

def welcome():
    styles.styled_print("Enter your name below: ")
    name = input()
    styles.welcome_message(f"Hello {name} and welcome to the World Of Games: The Epic Journey")


def start_play():
    games = {
        1: "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
        2: "Guess Game - guess a number and see if you chose like the computer.",
        3: "Currency Roulette - try and guess the value of a random amount of USD in ILS."
    }
    games_list = [memory_game, guess_game, currency_roulette_game]

    styles.menu_items("Please choose a game to play:")
    for key, value in games.items():
        print(f"{key}. {value}")

    while True:
        styles.menu_items("Select your game (1-3): ")
        choice = input()
        try:
            choice = int(choice)
            if choice in games:
                while True:
                    styles.menu_items("Choose a difficulty (1-5): ")
                    difficulty_choice = input()
                    try:
                        difficulty_choice = int(difficulty_choice)
                        if 1 <= difficulty_choice <= 5:
                            styles.choice_result(f"Your difficulty is {difficulty_choice}")
                            styles.choice_result(f"Your game is: {games[choice]}")
                            styles.choice_result("Initiating...")
                            if games_list[choice-1].play(difficulty_choice):
                                print(f"Congratulations! You won!")
                                score.add_score(difficulty_choice)
                            return
                        else:
                            styles.error_message(error_message_1_to_5)
                    except ValueError:
                        print(invalid_input)
            else:
                styles.error_message(error_message_1_to_3)
        except ValueError:
            print(invalid_input)
