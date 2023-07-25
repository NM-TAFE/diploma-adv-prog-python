from __future__ import annotations
from demo_code import hello
from typing import Sequence


class Cat:
    def play(self, another_cat: Cat) -> str:
        pass



def pat_cat(cat: Cat):
    pass







def welcome(name: str | None = None, age: int = 45) -> str:
    if not name:
        name = "why don't you give me a name"
    return f'Hello {"old" if age > 40 else "young"} {name}'


def welcome_many(names: Sequence[str]):
    return '\n'.join(
        [welcome(name) for name in names]
    )



print(welcome_many(
    ['Raf',
     'Faf',
     'Smaf']
))
