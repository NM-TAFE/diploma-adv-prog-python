class Dog:
    name = "Fido"
class Cat:
    def __init__(self, name: str):
        self.name = name

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return f"Cat({self.name!r})"

print(
    Cat("Charlie") < Dog()
)
