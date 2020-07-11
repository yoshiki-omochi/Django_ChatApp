from django.shortcuts import render

# Create your views here.

from django.views import generic

from django.http import HttpResponse
from Chat.forms import UserForm

from django.views import View

from .models import User

from . import models,forms




class IndexView(generic.TemplateView):
    template_name = "index.html"

class FooView(generic.TemplateView):
    template_name = "foo.html"

class PostView(View): 
    def get(self, request, *args, **kwargs):
        f = UserForm()
        return render(request, 'post.html', {'form1' : f})

    def post(self, request, *args, **kwargs):
        context = {
            'name' : request.POST['name'],
            'email': request.POST['email'],
            'comment': request.POST['comment'],
        }
        

        user_form = UserForm(request.POST or None)
        if user_form.is_valid():
            user_form.save()

        return render(request, 'posted.html', context)


def timeline(request):
    #user_form = UserForm(request.POST or None)
    

    data = User.objects.all()
    parms  = {
        'message' : '投稿者',
        'data': data, 
    }
    return render(request, 'timeline.html', parms)


class TimelineView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'timeline.html', User)


