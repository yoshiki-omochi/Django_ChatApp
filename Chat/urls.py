from django.urls import path 
from . import views

app_name = 'Chat'

urlpatterns = [
    path('',views.IndexView.as_view(), name = 'index'),
    path('foo/',views.FooView.as_view(), name = 'foo'),
    path('post/',views.PostView.as_view(), name = 'post'),
    path('timeline/',views.timeline,  name = 'timeline')
]
