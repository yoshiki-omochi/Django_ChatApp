from django.shortcuts import render

# Create your views here.

from django.views import generic

from django.http import HttpResponse
from Chat.forms import TestuserForm

from django.views import View



class IndexView(generic.TemplateView):
    template_name = "index.html"

class FooView(generic.TemplateView):
    template_name = "foo.html"

class PostView(View):
    
    def get(self,request,*args,**kwargs):
        f = TestuserForm()
        return render(request, 'post.html', {'form1' : f})

    def post(self, request, *args, **kwargs):
        f = TestuserForm()
        return render(request, 'post.html', {'form1' : f})
        
    


class TimelineView(generic.TemplateView):
    template_name = "timeline.html"


