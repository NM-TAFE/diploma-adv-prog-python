import logging
import asyncio

# factory
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

# observer
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


# decorator
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

# generator
def read_logs(log_file_path):
    with open(log_file_path, 'r') as file:
        for line in file:
            yield line.strip()

for line in read_logs('logs.txt'):
    print('Log: ', line)

# synchrounous
async def fetch_metadata(doc):
    async with aiohttp.ClientSession() as session:
        url = f"https://jsonplaceholder.typicode.com/users"


    async with session.get(url) as response:
        data = await response.json()
        print(f"Doc {doc}: {data['title']}")

async def fetch_all_metadata():
    await asyncio.gather(
        fetch_metadata(1),
        fetch_metadata(2),
        fetch_metadata(3)
    )

asyncio.run(fetch_all_metadata())