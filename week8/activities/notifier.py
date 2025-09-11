import logging

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

# print(users)


class UploadNotifier:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, fn):
        self.subscribers.append(fn)

    def notify(self, document_name):
        for fn in self.subscribers:
                fn(document_name)

def alert_admin(doc):
    logging.info(f"Admin notified: {doc} uploaded")

def log_upload(doc):
    logging.info(f"Log notified: {doc} uploaded buy")


notifier = UploadNotifier()
notifier.subscribe(alert_admin)
notifier.subscribe(log_upload)



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def action_logger(func):
    def wrapper(*args, **kwargs):
        user = args[0]
        logging.info(f"[ACTION] {user.name} ({user.role()}) has run {func.__name__}")
        return func(*args, **kwargs)

    return wrapper

@action_logger
def upload_document(user, document):
    print(f'{user.name} ({user.role()}), uploaded {document}')
    notifier.notify(document)


upload_document(users[0], 'project_plan_v1.pdf')