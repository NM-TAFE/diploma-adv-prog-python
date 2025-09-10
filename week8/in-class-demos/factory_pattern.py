class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    pass

class Guest(User):
    pass

def create_user(user_type, name):
    if user_type == "admin":
        return Admin(name)
    elif user_type == "guest":
        return Guest(name)

user = create_user("guest", "Jamie")
print(isinstance(user, Guest))  # True
user = create_user("admin", "Jamie")
print(isinstance(user, Guest))  # False