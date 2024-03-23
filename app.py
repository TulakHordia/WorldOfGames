def welcome():
    name = input("Enter your name below: ")
    print(f"Hi {name} and welcome to the World Of Games: The Epic Journey")


def start_play():
    choice_prompt = "Please choose a game to play: "
    mem_game = "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back."
    guess_game = "2. Guess Game - guess a number and see if you chose like the computer."
    currency_game = "3. Currency Roulette - try and guess the value of a random amount of USD in ILS."
    games_list = [choice_prompt, mem_game, guess_game, currency_game]
    game_names = ['Memory Game', 'Guess Game', 'Currency Roulette']

    for x in games_list:
        print(x)
    while True:
        choice = int(input("Select your game (1-3): "))
        if choice in range(1, 4):
            while True:
                difficulty_choice = int(input("Choose a difficulty (1-5): "))
                if difficulty_choice in range(1, 6):
                    print(f"Your difficulty is {difficulty_choice}")
                    break
                else:
                    print("Invalid input, Difficulty must be between 1 and 5")
            print(f"Your game is {game_names[choice - 1]}")
            break
        else:
            print("Invalid input, Please select a number between 1 and 3")
