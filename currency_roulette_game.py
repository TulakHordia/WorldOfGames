import random
import requests
import styles


def get_exchange_rates():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    exchange_rate = data['rates']['ILS']
    return exchange_rate


def get_money_interval(difficulty):
    exchange_rate = get_exchange_rates()
    difference = 10 - difficulty
    return difference


def get_guess_from_user():
    user_guess = int(input('Guess the value for the converted value: '))
    return user_guess


def compare_results(interval, guess, currency_in_ils):
    min_val = currency_in_ils - interval
    max_val = currency_in_ils + interval
    if min_val < guess < max_val:
        return True
    else:
        return False


def play(difficulty):
    secret_number_in_usd = random.randint(1, 100) # In USD
    exchange_rate = get_exchange_rates() # USD to ILS exchange rate
    secret_number_in_ils = int(exchange_rate * secret_number_in_usd) # In ILS
    interval = get_money_interval(difficulty)
    guess = get_guess_from_user()
    if compare_results(interval, guess, secret_number_in_ils):
        print('Congrats! You guessed the correct value!')
        styles.choice_result(f"Correct value is: {secret_number_in_ils}")
    else:
        print('Sorry, you guessed the wrong value!')
        styles.error_message(f"The correct value was: {secret_number_in_ils}")
