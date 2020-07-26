from django.shortcuts import render,redirect


from django.http import HttpResponse #requestを使うために必要
from accounts.forms import SignUpUserForm
from accounts.forms import LoginForm
from django.views import View
from . import models,forms
from django.views import generic

from django.contrib.auth import authenticate #usernameとpasswordを認証するときに必要
from django.contrib.auth import login #ログインのため


class SignUpView(View):

    #GETリクエストを受け取ったとき
    def get(self, request, *args, **kwargs):
        form = SignUpUserForm()
        return render(request, 'signupget.html', {'form' : form})


    #POSTリクエストを受け取ったとき
    def post(self, request, *args, **kwargs):

        #レンダリングするための値を、辞書型で変数に代入
        signin_contexts = {
            'username' : request.POST['username'],
            'email' : request.POST['email'],
            'password' : request.POST['password'],
        }
        
        #データベースに代入する値を変数に代入し、.save()で保存する
        signin_user_form = SignUpUserForm(request.POST or None)
        if signin_user_form.is_valid():
            signin_user_form.save()

        #遷移後の画面を表示させるためにレンダリングする
        return render(request, 'signuppost.html', signin_contexts)




class LoginView(View):
    #GETリクエストを受け取ったとき
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form' : form})

    #POSTリクエストを受け取ったとき
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        #formが有効だった（blankやnullの条件を満たしている）場合、dbに保存
        if form.is_valid:
            form.save()

            #フォームからusernameを読み取る
            username = form.cleaned_data.get('username')
            print(username)
            #フォームからパスワードを読み取る
            password = form.cleaned_data.get('password')
            print(password)
            #名前とパスワードを認証する
            user = authenticate(username = 'admin', password = 'password')
            if user is not None:
                if user.is_active:
                    print ("You provided a correct username and password!")
                else:
                    print ("Your account has been disabled!")
                

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html',{'form' : form})


        #return render(request, 'login.html',{'form' : form})




#ログイン後に表示するページ
def home(request):
        return render(request, 'Chat/index.html')