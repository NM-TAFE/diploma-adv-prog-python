class Cat[V]:
    lives = 9
    @classmethod
    def get_total_lives(cls):
        return cls.lives

cat = Cat[str]()
