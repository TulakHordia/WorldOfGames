def welcome():
    name = input("Enter your name below: ")
    print(f"Hi {name} and welcome to the World Of Games: The Epic Journey")


def start_play():
    games = {
        1: "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
        2: "Guess Game - guess a number and see if you chose like the computer.",
        3: "Currency Roulette - try and guess the value of a random amount of USD in ILS."
    }

    print("Please choose a game to play:")
    for key, value in games.items():
        print(f"{key}. {value}")

    while True:
        choice = int(input("Select your game (1-3): "))
        if choice in games:
            while True:
                difficulty_choice = int(input("Choose a difficulty (1-5): "))
                if 1 <= difficulty_choice <= 5:
                    print(f"Your difficulty is {difficulty_choice}")
                    print(f"Your game is {games[choice]}")
                    return
                else:
                    print("Invalid input, Difficulty must be between 1 and 5")
        else:
            print("Invalid input, Please select a number between 1 and 3")


welcome()
start_play()
