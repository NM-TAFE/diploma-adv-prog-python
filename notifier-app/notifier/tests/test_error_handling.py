from django.test import TestCase
from notifier.services.delivery import (
    NotificationRequest,
    safe_send_notification,
    NotificationDeliveryError,
)

class ErrorHandlingExamples(TestCase):
    def setUp(self):
        self.request = NotificationRequest(
            recipient_email="student@example.com",
            subject="Session 14 Reminder",
            message="Audit your tests before stand-up.",
        )

        def test_safe_send_notification_handles_success(self):
            def send_callable(request):
                return "message-123"

            payload = safe_send_notification(self.request, send_callable)

            self.assertEqual(payload["status"], "success")
            self.assertEqual(payload["message_id"], "message-123")

        def test_safe_send_notification_returns_template_on_error(self):
            def failing_sender(request):
                raise NotificationDeliveryError("Notification service unavailable.")

            payload = safe_send_notification(self.request, failing_sender)

            self.assertEqual(payload["status"], "error")
            self.assertIn("notification-error", payload["template"])
            self.assertIn(self.request.subject, payload["template"])