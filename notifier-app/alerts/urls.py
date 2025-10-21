from django.urls import path # URL helper
from . import views
from .views import upload_recipients

app_name = "alerts" # Namespacing
urlpatterns = [
    path('upload', upload_recipients, name="upload_recipients"),
    path("preview", views.preview_recipients, name="preview_recipients")# New upload route
]