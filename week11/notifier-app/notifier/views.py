import json
import asyncio
import logging

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required

from notifier.models import Document
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

@login_required
# one of 4 crud permissions
@permission_required("notifier.view_document", raise_exception=True)
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
        data = [serialise_document(doc) for doc in documents]
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

        return JsonResponse(serialise_document(document), status=201)

    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def document_detail(request, pk):
    try:
        document = Document.objects.get(pk=pk)
    except Document.DoesNotExist:
        return JsonResponse({"error": "Document not found."}, status=404)

    if request.method == "GET":
        return JsonResponse(serialise_document(document))

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
        return JsonResponse(serialise_document(document))

    if request.method == "DELETE":
        document.delete()
        return HttpResponse(status=204)

    return HttpResponseNotAllowed(["GET", "PUT", "PATCH", "DELETE"])
