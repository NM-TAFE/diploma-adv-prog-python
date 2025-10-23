from django.views.generic import ListView
from notifier.models import Notification

class NotificationListView(ListView):
    model = Notification
    queryset = Notification.objects.select_related("document", "recipient")
    template_name = "notifier/notification_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notifications = context["object_list"]
        context["total_queued"] = notifications.filter(status="queued").count()
        context["total_sent"] = notifications.filter(status="sent").count()
        context["total_failed"] = notifications.filter(status="failed").count()

        return context