from django.shortcuts import render


from django.http import HttpResponse #requestを使うために必要
from accounts.forms import SignUpUserForm
from django.views import View
from . import models,forms
from django.views import generic


class SignUpView(View):

    #GETリクエストを受け取ったとき
    def get(self, request, *args, **kwargs):
        form = SignUpUserForm()
        return render(request, 'signupget.html', {'form' : form})


    #POSTリクエストを受け取ったとき
    def post(self, request, *args, **kwargs):

        #レンダリングするための値を、辞書型で変数に代入
        signin_contexts = {
            'name' : request.POST['name'],
            'email' : request.POST['email'],
            'pass' : request.POST['pass'],
        }
        
        #データベースに代入する値を変数に代入し、.save()で保存する
        signin_user_form = SignUpUserForm(request.POST or None)
        if signin_user_form.is_valid():
            signin_user_form.save()

        return render(request, 'signuppost.html', signin_contexts)