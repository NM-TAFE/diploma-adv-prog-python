
class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'🐈{self.name}🐈'


    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.name!r})'

class Kitten(Cat):
    ...

c = Cat("Lenny")
b = Cat("Lenny")
print(c == b)