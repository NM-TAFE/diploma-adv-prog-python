from some_vars import *
class Cat:
    x = 42
    __hello = 24

class __Pet(Cat):
    __hello = "bla"
    x = 99
    def __init__(self):
        print(self.x)
        print(self.__hello)
        print(self._Cat__hello)
        print(self._Pet__hello)
p = Pet()
print()