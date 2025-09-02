from typing import Any

def sum_of_chars(data: Any) -> int:
    return sum(
        ord(char) for char in str(data)
    ) % 256


def sum_of_chars(data: Any, size: int = 256) -> int:
    data = str(data)
    total = 0
    for char in data:
        total += ord(char)

    return total % size


def read_file():
    with open("lyrics.txt") as f:
        return f.read()

def main():
    print(sum_of_chars("Hello, World!"))
    print(sum_of_chars("Hello!"))
    print(sum_of_chars("World!"))
    print(sum_of_chars("World"))
    print(sum_of_chars(read_file()))

if __name__ == '__main__':
    main()
