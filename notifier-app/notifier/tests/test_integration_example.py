import asyncio
import json
from typing import List
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from notifier.models import Document

async def fake_metadata_fetch() -> List[str]:
    await asyncio.sleep(0)
    return ["stubbed"]


class NotifyViewIntegrationTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.password = "password1"
        self.user = user_model.objects.create_user(
            username="lecturer",
            email="lecturer@example.com",
            password=self.password,
        )
        permission = Permission.objects.get(codename="view_document")
        self.user.user_permissions.add(permission)
        assert self.client.login(username=self.user.username, password=self.password)


    @patch("notifier.views.views.fetch_all_metadata", new=fake_metadata_fetch)
    def test_notify_view_context(self):
        response = self.client.get(reverse("notify"))
        self.assertEqual(response.status_code, 200)
        context = response.context

        self.assertIn("logs", context)
        self.assertIn("user", context)
        self.assertGreater(len(context["logs"]), 0)
        self.assertEqual(context["user"].name, "Ben")