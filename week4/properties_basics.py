from typing import Any, Optional
class Cat:
    def __init__(self, lives: int):
        self._lives = 9
        self._is_alive = True

    @property
    def lives(self):
        return self._lives

    def kill_cat(self,
                 message: str | None = None):
        print(message)
        self._lives -= 1
        if self._lives == 0:
            self._is_alive = False

c = Cat()
c.kill_cat(42)