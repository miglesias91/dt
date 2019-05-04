from django import forms
from club.models import LogMessage

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("mensaje",)   # NOTE: the trailing comma is required