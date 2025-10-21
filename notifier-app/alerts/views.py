import pandas as pd # Data validation helper
from django.contrib import messages # To show error feedback
from django.shortcuts import redirect, render # To render templates and redirect
from .forms import RecipientUploadForm # Import upload form
from django.core.paginator import Paginator # Pagination utility
from django.http import HttpRequest
from django.utils.safestring import mark_safe # For safe HTML messages

REQUIRED_COLUMNS = {"email", "first_name", "last_name"} # Expected CSV schema

def upload_recipients(request): # Instantiate form with request data and files
    form = RecipientUploadForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid(): # Read uploaded file into DataFrame
        df = pd.read_csv(request.FILES["csv_file"]) # Calculate missing columns using set difference
        missing = REQUIRED_COLUMNS - set(df.columns.str.lower())

        if missing: # Surface validation error without storing file
            messages.error(request, f"Missing columns: {', '.join(sorted(missing))}")
        else: # TODO: Replace with model bulk_create or other persistence logic
            messages.success(request, f"Uploaded {len(df)} recipients successfully.")

            return redirect("alerts:preview_recipients") # Proceed to preview step # Render template with current form state

    return render(request, "alerts/upload_recipients.html", {"form": form})


def preview_recipients(request: HttpRequest): # Placeholder data until persistence is added; replace with session or DB query
    sample_data = [
        {"email": f"user{i}@example.com", "first_name": f"First{i}", "last_name": f"Last{i}"}
        for i in range(1, 51)
    ]

    paginator = Paginator(sample_data, 10) # Get requested page or default to 1
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number) # Provide page object to template

    return render(request, "alerts/preview_recipients.html", {"page_obj": page_obj})