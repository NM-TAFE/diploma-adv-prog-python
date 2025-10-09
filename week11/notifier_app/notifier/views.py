
import asyncio
import logging

from django.shortcuts import render
from notifier.utils.factories import create_user
from notifier.services.observer import UploadNotifier, alert_admin, log_upload
from notifier.services.logging import action_logger
from notifier.utils.log_reader import read_logs
from notifier.utils.metadata import fetch_all_metadata

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
