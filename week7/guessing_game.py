import random
from typing import Callable
from pathlib import Path




def get_secret(max_value: int) -> int:
    return random.randint(0, max_value)


def is_correct(guess: int, secret: int) -> bool:
    return guess == secret

def linear_ai(max_value: int, min_value: int = 0) -> int:
    """Performs a linear search"""
    return min_value

def binary_search_ai(max_value: int, min_value: int = 0) -> int:
    """Uses a hyper-intelligent (post-human) super binary
    search capabilities.
    """
    return min_value + (max_value - min_value)//2

def interactive(max_value: int, min_value: int = 0) -> int:
    """Human function"""

    while True:
        print(f"Please give a number between {min_value}-{max_value}")

        clue = min_value + (max_value - min_value) // 2
        guess = input(f'{min_value}-{max_value} ({clue})? ')

        try:
            return int(guess)
        except ValueError:
            print("Please enter a valid number")
            continue


def save_result(file: Path | str,
                tries: int,
                max_value: int,
                func: Callable,
                header: tuple[str] =
                ('func_name', 'tries', 'max_value')) -> None:

    if isinstance(file, str):
        file = Path(file)

    file.parent.mkdir(parents=True, exist_ok=True)
    file_is_empty = not file.exists() or file.stat().st_size == 0
    func_name = func.__name__

    with open(file, "a") as f:
        if file_is_empty:
            f.write(','.join(header) + '\n')
        f.write(f'{func_name},{tries},{max_value}\n')


def play(max_value: int,
         guess_function: Callable,
         file: Path | str | None = None):
    tries = 0
    og_max = max_value
    secret = get_secret(max_value)
    min_value = 0
    while True:
        guess = guess_function(max_value, min_value)
        tries += 1
        if is_correct(guess, secret):
            print("Well done! You Win!")
            if file:
                save_result(file, tries, og_max, guess_function)
            break
        elif guess < secret:
            min_value = guess + 1 if guess > min_value else min_value
            print("Guess higher")
        else:
            max_value = guess - 1 if guess < max_value else max_value
            print("Guess lower")


def activate_ai(file):
    for value in range(1000, 100_000, 1000):
        play(value, linear_ai, file)
        play(value, binary_search_ai, file)

def main():
    # play(1000, interactive, "game_results.csv")
    activate_ai("game_results.csv")


if __name__ == '__main__':
    main()
