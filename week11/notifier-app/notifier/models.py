from django.db import models


class Document(models.Model):
    """Represents a file uploaded to the notifier application."""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
