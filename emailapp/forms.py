# emailapp/forms.py

from django import forms

class EmailForm(forms.Form):
    recipient_email = forms.EmailField()
    message_text = forms.CharField(widget=forms.Textarea)
