import random
from typing import Callable
from pathlib import Path


def get_secret(max_value: int) -> int:
    return random.randint(0, max_value)


def is_correct(guess: int, secret: int) -> bool:
    return guess == secret


def interactive(max_value: int) -> int:
    min_value = 0
    while True:
        print(f"Please give a number between {min_value}-{max_value}")
        guess = input(f'{min_value}-{max_value}? ')
        try:
            return int(guess)
        except ValueError:
            print("Please enter a valid number")
            continue


def play(max_value: int,
         guess_function: Callable,
         file: Path | str | None = None):
    secret = get_secret(max_value)
    while True:
        guess = guess_function(max_value)
        if is_correct(guess, secret):
            print("Well done! You Win!")
            break
        elif guess < secret:
            print("Guess higher")
        else:
            print("Guess lower")



def main():
    play(100, interactive)


if __name__ == '__main__':
    main()
