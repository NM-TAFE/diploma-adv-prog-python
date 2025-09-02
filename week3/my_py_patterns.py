class Cat:
    _lives: int

    def __init__(self, lives: int):
        self._lives = lives


    @property
    def lives(self) -> int:
        return self._lives
