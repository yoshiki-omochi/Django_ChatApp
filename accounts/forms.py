from django import forms
from .models import CustomUser
from .models import LoginUser


#登録用のユーザモデルのためのフォーム
class SignUpUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password')


#ログインのためのフォーム
class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginUser
        fields = ('username', 'password')