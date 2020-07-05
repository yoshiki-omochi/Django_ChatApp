from django.urls import path 
from . import views

app_name = 'Chat'

urlpatterns = [
    path('',views.IndexView.as_view(), name = 'index'),
    path('foo/',views.FooView.as_view(), name = 'foo'),
    path('post/',views.post, name = 'post'),
    path('timeline/',views.TimelineView.as_view(), name = 'timeline')
]
