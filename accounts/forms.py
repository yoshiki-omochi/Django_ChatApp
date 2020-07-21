from django import forms
from .models import SignUpUser


class SignUpUserForm(forms.ModelForm):
    class Meta:
        model = SignUpUser
        fields = ('name','email','password')