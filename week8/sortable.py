class Cat:
    def __init__(self, name, cuteness):
        self.name = name
        self.cuteness = cuteness

    def __repr__(self):
        return f"Cat({self.name!r})"

    def __lt__(self, other):
        if isinstance(other, int):
            return self.cuteness < other
        if isinstance(other, Cat):
            return self.cuteness < other.cuteness
        return NotImplemented

    def __gt__(self, other):
        raise NotImplementedError
        if isinstance(other, int):
            return self.cuteness > Cat("", other)
        if isinstance(other, Cat):
            return self.cuteness > other.cuteness
        return NotImplemented


# class Dog:
#     def __
# cats = [Cat('Lenny', 100_000),
#         Cat('Kenny', 1_000_000),
#         10_000]
lenny = Cat("Lenny", 42)
lenny.__gt__(42)
lenny > 42