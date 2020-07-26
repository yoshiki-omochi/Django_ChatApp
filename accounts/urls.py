from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
   # path('login', views.LoginView.as_view(), name = 'login'), #ログイン画面
   # path('logout', view.LogoutView.as_view(), name = 'logout') , #ログアウト画面
    path('signup', views.SignUpView.as_view(), name = 'signup'), #サインアップ（エントリー画面）
   # path('confirm-email', views.ConfirmEmail.as_view(), name = 'confirmemail'), #サインアップ（メール送信）
   # path('password/reset/', view.PassResetView.as_view(), name = 'passreset') , #パスワードリセット（エントリー画面）
   # path('password/reset/done/', view.PassResetDoneView.as_view(), name = 'passresetdone'), #パスワードリセット（メール送信）
   # path('),#パスワードの再設定画面(pkを使った値を使いそう)
    path('login/',  views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]