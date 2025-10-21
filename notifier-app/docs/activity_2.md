postman## Activity 2 – Building CRUD APIs for the Notifier App

### Model the data

- Define a `Document` model in `notifier/models.py` with `title`, `description`, and `uploaded_at` fields.
- Create and inspect the initial migration that introduces the new model.`bash python manage.py migrate`
- Verify the migration references the existing `db.sqlite3` database in `notifier_core/settings.py`.

### Implement CRUD endpoints

- Add helper code that converts `Document` instances into JSON-friendly dictionaries.
- Build two view functions: one that handles `GET` and `POST` requests for `/api/documents/`, and another that supports `GET`, `PUT/PATCH`, and `DELETE` for `/api/documents/<id>/`.
- Wire the new views into `notifier/urls.py`, following Django’s URL dispatcher patterns.

## Validation & Response Control

- Ensure the create endpoint validates payloads (e.g. `title` is required) and returns useful HTTP status codes.
- Reuse the existing notifier workflow when a document is created so uploads still trigger log entries.
- Decide how the API should respond if clients request a document that does not exist.

### Manual verification & docs

- Apply migrations and spin up the development server.
- Exercise the new endpoints with `curl` or an API client to confirm they behave as expected.
- Record any setup notes or caveats in the project README.

# models.py

```python
from django.db import models


class Document(models.Model):
    """Represents a file uploaded to the notifier application."""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
```

# 0001_initial.py

```python
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
```

# urls.py

```python
# from django.urls import path

# from .views import (
#     notify_view,
    documents_collection,
    document_detail,
# )

# urlpatterns = [
#     path('', notify_view, name='home'),
#     path('notify/', notify_view, name='notify'),
    path('api/documents/', documents_collection, name='documents_collection'),
    path('api/documents/<int:pk>/', document_detail, name='document_detail'),
# ]
```

# views.py

```python
# import json
# import asyncio
# import logging

# from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from notifier.models import Document
# from notifier.utils.factories import create_user
# from notifier.services.observer import UploadNotifier, alert_admin, log_upload
# from notifier.services.logging import action_logger
# from notifier.utils.log_reader import read_logs
# from notifier.utils.metadata import fetch_all_metadata

# notifier = UploadNotifier()
# notifier.subscribe(alert_admin)
# notifier.subscribe(log_upload)

# @action_logger
# def upload_document(user, document_name):
# notifier.notify(document_name)

# def notify_view(request):
# logging.basicConfig(level=logging.INFO)

#     user = create_user("admin", "Ben")
#     upload_document(user, "project_plan.pdf")

#     logs = []
#     try:
#         for line in read_logs("notifier/logs.txt"):
#             logs.append(line)
#     except FileNotFoundError:
#         logs.append("No logs yet.")

#     asyncio.run(fetch_all_metadata())

#     return render(request, "notifier/index.html", {
#         "user": user,
#         "logs": logs
#     })

def serialise_document(document: Document) -> dict:
    return {
        "id": document.id,
        "title": document.title,
        "description": document.description,
        "uploaded_at": document.uploaded_at.isoformat().replace("+00:00", "Z"),
    }

@csrf_exempt
def documents_collection(request):
    if request.method == "GET":
    documents = Document.objects.order_by("-uploaded_at")
    data = [serialize_document(doc) for doc in documents]
    return JsonResponse({"documents": data})

        if request.method == "POST":
            try:
                payload = json.loads(request.body or "{}")
            except json.JSONDecodeError:
                return HttpResponseBadRequest("Invalid JSON payload.")

            title = payload.get("title")
            if not title:
                return JsonResponse({"error": "title is required."}, status=400)

            description = payload.get("description", "")
            document = Document.objects.create(title=title, description=description)

            return JsonResponse(serialize_document(document), status=201)

        return HttpResponseNotAllowed(["GET", "POST"])

@csrf_exempt
def document_detail(request, pk):
    try:
        document = Document.objects.get(pk=pk)
    except Document.DoesNotExist:
        return JsonResponse({"error": "Document not found."}, status=404)

        if request.method == "GET":
            return JsonResponse(serialize_document(document))

        if request.method in {"PUT", "PATCH"}:
            try:
                payload = json.loads(request.body or "{}")
            except json.JSONDecodeError:
                return HttpResponseBadRequest("Invalid JSON payload.")

            if "title" in payload:
                title = payload["title"]
                if not title:
                    return JsonResponse({"error": "title cannot be empty."}, status=400)
                document.title = title

            if "description" in payload:
                document.description = payload["description"] or ""

            document.save()
            return JsonResponse(serialize_document(document))

        if request.method == "DELETE":
            document.delete()
            return HttpResponse(status=204)

        return HttpResponseNotAllowed(["GET", "PUT", "PATCH", "DELETE"])
```

### Additional task

### Test the API

- Use Django’s `TestCase` and the test client to write unit tests in `notifier/tests.py` that cover each CRUD operation.
- Focus on observable behaviour: status codes, JSON payloads, and database state.
- Run the test suite to confirm everything passes.

# tests.py

```python
import json

from django.test import TestCase
from django.urls import reverse

from notifier.models import Document


class DocumentAPITest(TestCase):

    def test_create_document_and_list(self):
        payload = {"title": "Project Plan", "description": "Initial draft"}
        create_response = self.client.post(
            reverse("documents_collection"),
            data=json.dumps(payload),
            content_type="application/json",
        )
        self.assertEqual(create_response.status_code, 201)

        list_response = self.client.get(reverse("documents_collection"))
        self.assertEqual(list_response.status_code, 200)
        documents = list_response.json()["documents"]
        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0]["title"], payload["title"])
        self.assertEqual(documents[0]["description"], payload["description"])

    def test_update_document(self):
        document = Document.objects.create(title="Doc", description="")
        payload = {"title": "Updated Doc", "description": "Revised version"}

        response = self.client.patch(
            reverse("document_detail", args=[document.pk]),
            data=json.dumps(payload),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        document.refresh_from_db()
        self.assertEqual(document.title, payload["title"])
        self.assertEqual(document.description, payload["description"])

    def test_delete_document(self):
        document = Document.objects.create(title="Doc", description="")

        response = self.client.delete(reverse("document_detail", args=[document.pk]))

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Document.objects.filter(pk=document.pk).exists())
```
