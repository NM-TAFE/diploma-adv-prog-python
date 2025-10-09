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
