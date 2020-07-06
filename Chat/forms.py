from django import forms
from .models import TestUser


    
class TestuserForm(forms.ModelForm):
    class Meta:
        model = TestUser
        fields = ('name','email','comment',)  