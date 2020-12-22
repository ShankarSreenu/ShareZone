from django import forms
from .models import message

class MessageForm(forms.ModelForm):
    class Meta:
        model = message
        fields = ['to_user','text']
        