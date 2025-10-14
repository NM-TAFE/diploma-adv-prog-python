class Pet:
    def __hash__(self):
        print("I am in Pet")
        return 42


class BST:
    root = "Whatever"
    def _insert(self, node, current_root):
        ...
    def insert(self, node):
        ...

class Cat:
    cat_ids = []
    def __new__(cls, *args, **kwargs):

    def __init__(self):
        self.key = Pet()

    def __hash__(self):
        print("I am in Cat!")
        return hash

    def meow(key: str):
        print("Meow", key.upper(), type(key))

print(sorted(['ccc', 'aa', 'b'], key=len))


print('ccc' == 'aaa')
print(hash('ccc'.__len__) == hash('aaa'.__len__))
print('ccc' == 'ccc')
print(hash('ccc') == hash('ccc'))
c = Cat()
c.meow()
c.meow = 42
Cat.meow = 42
type(c).meow(c)
Cat.meow(c)


