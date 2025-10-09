import asyncio
import aiohttp
import logging

# Step 1: Factory Pattern – User Creation
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

# Sample users
users = [
    create_user("Admin", "Pui"),
    create_user("Editor", "Maddie"),
    create_user("Viewer", "Gian Carlo")
]

# Step 2: Observer Pattern – Notify on Upload
class UploadNotifier:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, fn):
        self.subscribers.append(fn)

    def notify(self, doc_name):
        for fn in self.subscribers:
            fn(doc_name)

# Example subscriber functions
def alert_admin(doc):
    logging.info(f"[ALERT] Admin notified: '{doc}' uploaded.")

def log_upload(doc):
    logging.info(f"[LOG] Document '{doc}' was uploaded.")

notifier = UploadNotifier()
notifier.subscribe(alert_admin)
notifier.subscribe(log_upload)

# Step 3: Decorator – Log User Actions
# Setup basic config for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def action_logger(func):
    def wrapper(*args, **kwargs):
        user = args[0]  # first argument is always the User object
        logging.info(f"[ACTION] {user.name} ({user.role()}) is performing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@action_logger
def upload_document(user, document_name):
    print(f"{user.name} uploaded '{document_name}'")
    print(f"[ACTION] {user.name} ({user.role()}), uploaded {document_name}")
    notifier.notify(document_name)

upload_document(users[0], "project_plan.pdf")

# Step 4: Generator – Simulate Reading Log Lines
def read_logs(log_file_path):
    with open(log_file_path, "r") as file:
        for line in file:
            yield line.strip()

# Simulate reading logs
for line in read_logs("logs.txt"):
    print("Log:", line)

# Step 5: Async/Await – Fetch Document Metadata
async def fetch_metadata(doc_id):
    async with aiohttp.ClientSession() as session:
        url = f"https://jsonplaceholder.typicode.com/posts/{doc_id}"
        async with session.get(url) as response:
            data = await response.json()
            print(f"[METADATA] Doc {doc_id}: {data['title']}")

async def fetch_all_metadata():
    await asyncio.gather(
        fetch_metadata(1),
        fetch_metadata(2),
        fetch_metadata(3)
    )

# Run this at the end of the script
asyncio.run(fetch_all_metadata())

