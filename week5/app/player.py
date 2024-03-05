from custom_hashing import pearson_hash

class Player:
    name: str
    uid: str

    def __init__(self, uid, name):
        self.name = name
        self.uid = uid


    def __eq__(self, other):
        return (
                isinstance(other, Player) and
                self.uid == other.uid
        )

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self.name!r}, {self.uid!r})"


    def __hash__(self) -> int:
        return self.make_hash(self.uid)

    @staticmethod
    def make_hash(key):
        return pearson_hash(key)
