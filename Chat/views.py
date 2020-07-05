from django.shortcuts import render

# Create your views here.

from django.views import generic

from django.http import HttpResponse
from Chat.forms import UserForm



class IndexView(generic.TemplateView):
    template_name = "index.html"

class FooView(generic.TemplateView):
    template_name = "foo.html"

class PostView(generic.TemplateView):
    template_name = "post.html"

class TimelineView(generic.TemplateView):
    template_name = "timeline.html"


def post(request):
    f = UserForm()
    return render(request, 'post.html', {'form1' : f})