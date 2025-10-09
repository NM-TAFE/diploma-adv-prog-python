## Notifcation App
Builds on the design pattern exercise in week 8 as an introduction to Django 
but with a focus on View logic and the seperation of concerns
Stage 2 will include model, templates and forms.

### Step 1: Setup Django Project in PyCharm

1. **Create a New Project in PyCharm**
   - File > New Project
   - Select “Pure Python”
   - Name it: `notifier_project`
   - Use a new virtual environment
   - Click **Create**

2. **Install Django & aiohttp**
   Open the PyCharm Terminal:

   ```bash
   pip install django aiohttp
   ```
⸻

### Step 2: Start the Django Project & App

Create the Django project (use underscore _ instead of dash -)
```bash
django-admin startproject notifier_core .
```

Create the Django app
```bash
python manage.py startapp notifier
````

⸻
### Step 3: Add App to Installed Apps

In notifier_core/settings.py, update:
```python
INSTALLED_APPS = [
    ...
    'notifier',
]

TEMPLATES = [
    {
        ...
        'APP_DIRS': True,
    }
]
```

⸻

### Step 4: Set Up Project Structure

In notifier/ app, create this structure:

```markdown
notifier/
├── core/
│   └── observer.py
├── utils/
│   ├── factories.py
│   ├── log_reader.py
│   └── metadata.py
├── decorators/
│   └── logging.py
├── templates/
│   └── notifier/
│       └── index.html
├── views.py
├── urls.py

``````
⸻

### Step 5: Add Core Code (Design Patterns)

⸻

utils/factories.py – Factory Pattern
```python
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
```
⸻

core/observer.py – Observer Pattern
```python
import logging

class UploadNotifier:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, fn):
        self.subscribers.append(fn)

    def notify(self, doc_name):
        for fn in self.subscribers:
            fn(doc_name)

def alert_admin(doc):
    logging.info(f"[ALERT] Admin notified: '{doc}' uploaded.")

def log_upload(doc):
    logging.info(f"[LOG] Document '{doc}' was uploaded.")
```

⸻

decorators/logging.py – Decorator Pattern

```python
import logging

def action_logger(func):
    def wrapper(*args, **kwargs):
        user = args[0]
        logging.info(f"[ACTION] {user.name} ({user.role()}) is performing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

⸻

utils/log_reader.py – Generator Pattern
```python
def read_logs(log_file_path):
    with open(log_file_path, "r") as file:
        for line in file:
            yield line.strip()
```

⸻

utils/metadata.py – Async/Await
```python
import aiohttp
import asyncio

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
        fetch_metadata(3),
    )

```
⸻

### Step 6: Views and URLs
views.py

```python

from django.shortcuts import render
from notifier.utils.factories import create_user
from notifier.services.observer import UploadNotifier, alert_admin, log_upload
from notifier.services.logging import action_logger
from notifier.utils.log_reader import read_logs
from notifier.utils.metadata import fetch_all_metadata
import asyncio
import logging

notifier = UploadNotifier()
notifier.subscribe(alert_admin)
notifier.subscribe(log_upload)


@action_logger
def upload_document(user, document_name):
    notifier.notify(document_name)


def notify_view(request):
    logging.basicConfig(level=logging.INFO)

    user = create_user("admin", "Ben")
    upload_document(user, "project_plan.pdf")

    logs = []
    try:
        for line in read_logs("notifier/logs.txt"):
            logs.append(line)
    except FileNotFoundError:
        logs.append("No logs yet.")

    asyncio.run(fetch_all_metadata())

    return render(request, "notifier/index.html", {
        "user": user,
        "logs": logs
    })

```
⸻

notifier/urls.py
```python
from django.urls import path
from .views import notify_view

urlpatterns = [
    path('', notify_view, name='home'),
    path('notify/', notify_view, name='notify'),
]
```
⸻

notifier_core/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notifier.urls')),
]
```

⸻

### Step 7: Create Template

notifier/templates/notifier/index.html
```html
<!--{% load static %}-->
<!DOCTYPE html>
<html>
<head>
    <title>Notifier</title>
    <!--Uncomment  at step 12
    <link rel="stylesheet" href="{% static 'notifier/styles.css' %}">-->
</head>
<body>
    <h2>Hello {{ user.name }} ({{ user.role }})</h2>
    <p>Upload and notification triggered.</p>

    <h3>Logs:</h3>
    <ul>
      {% for log in logs %}
        <li>{{ log }}</li>
      {% endfor %}
    </ul>
</body>
</html>
```

⸻
### Step 8: Create Sample Log File

Create a file at:
notifier/logs.txt

```bash
System initialized
User uploaded file
Notification sent
```

⸻

### Step 9: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
This sets up the necessary database tables (users, sessions, etc.)

```markdown
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
⸻

### Step 10: Create Django Superuser (Optional for Admin Panel)
```bash
python manage.py createsuperuser
```

Follow the prompts:
	•	Username
	•	Email
	•	Password

Then you can log into the admin panel at:
http://127.0.0.1:8000/admin/

⸻

### Step 12: Add Static Files Support
1.	Create Static Folder:

```bash
  mkdir -p notifier/static/notifier
```
2.	Create CSS file: notifier/static/notifier/styles.css
```css
body {
    background-color: #f7f7f7;
    font-family: Arial, sans-serif;
    color: #333;
    padding: 20px;
}

h2 {
    color: #0066cc;
}
```
3.	Ensure this is loaded in your HTML
4.  No additional settings are required during development if DEBUG = True

⸻

### Step 12: Run the Server
```bash
python manage.py runserver
```

Visit:
http://127.0.0.1:8000/

You should see:
	•	Greeting from sample user
	•	Logs from file
	•	Observer pattern in action
	•	Async metadata printed in terminal

⸻
```markdown
TemplateDoesNotExist: notifier/index.html	File should be in notifier/templates/notifier/index.html and APP_DIRS=True
404 at /	Add empty path to notifier/urls.py and include it in project URLs
No module named manage	Use python manage.py, not python -m manage
Unapplied migrations	Run python manage.py migrate
Can’t log into admin	Run python manage.py createsuperuser
```
⸻


