from colorama import init, Fore, Style

init()


def styled_print(text):
    print(Style.NORMAL + Fore.LIGHTBLUE_EX + text + Style.RESET_ALL)


def welcome_message(text):
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)


def menu_items(text):
    print(Style.NORMAL + Fore.BLUE + text + Style.RESET_ALL)


def choice_result(text):
    print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)


def error_message(text):
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)