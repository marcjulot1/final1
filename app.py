import os
import command


def get_option_choice(options):
    """
    1. Prompt the user to enter a choice, using Python’s built-in input function.
    2. If the user’s choice matches one of those listed, call that option’s choose method.
    3. Otherwise, repeat.
    """
    choice = input("Choose an option: ")
    while not option_choice_is_valid(choice, options):
        print("Invalid choice")
        choice = input("Choose an option: ")
    return options[choice.upper()]
