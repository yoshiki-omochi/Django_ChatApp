from django import forms
from .models import User

class UserForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    
    