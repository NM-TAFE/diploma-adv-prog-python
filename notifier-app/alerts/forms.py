from django import forms # Form helpers

class RecipientUploadForm(forms.Form):
    csv_file = forms.FileField(label="Recipient CSV")