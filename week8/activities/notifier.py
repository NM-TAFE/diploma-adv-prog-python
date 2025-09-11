class User:
    def __init__(self, name):
        self.name = name

    def role(self):
        return "Default User"

class Admin(User):
    def role(self):
        return 'Admin'

class Editor(User):
    def role(self):
        return 'Editor'

class Viewer(User):
    def role(self):
        return 'Viewer'

def create_user(type, name):
    user_type = type.lower()

    match user_type:
        case 'admin':
            return Admin(name)
        case 'editor':
            return Editor(name)
        case 'viewer':
            return Viewer(name)
        case _:
            return Viewer(name)

users = [
    create_user('admin', 'John'),
    create_user('editor', 'Ben'),
    create_user('viewer', 'Zac'),
    create_user('admin', 'Dylan'),
]

print(users)

