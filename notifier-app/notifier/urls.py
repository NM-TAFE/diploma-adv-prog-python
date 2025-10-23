from django.urls import path

from .views import (
    notify_view,
    documents_collection,
    document_detail, dashboard,
)

from notifier.views import NotificationListView

urlpatterns = [
    path('/', notify_view, name='home'),
    path('notify/', notify_view, name='notify'),
    path('api/documents/', documents_collection, name='documents_collection'),
    path('api/documents/<int:pk>', document_detail, name='document_detail'),
    path('dashboard/', dashboard, name='dashboard'),
    path("notifications/", NotificationListView.as_view(), name="notification_list"),
]
