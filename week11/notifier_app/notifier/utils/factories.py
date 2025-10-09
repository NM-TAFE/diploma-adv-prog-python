class User:
    def __init__(self, name):
        self.name = name

    def role(self):
        return "Generic User"

class Admin(User):
    def role(self):
        return "Admin"

class Editor(User):
    def role(self):
        return "Editor"

class Viewer(User):
    def role(self):
        return "Viewer"

def create_user(user_type, name):
    user_type = user_type.lower()
    if user_type == "admin":
        return Admin(name)
    elif user_type == "editor":
        return Editor(name)
    elif user_type == "viewer":
        return Viewer(name)
    else:
        return User(name)