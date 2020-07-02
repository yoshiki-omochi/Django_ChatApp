from django.shortcuts import render

# Create your views here.

from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "index.html"



class FooView(generic.TemplateView):
    template_name = "foo.html"