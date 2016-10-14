from django.conf.urls import patterns, url 
from tutorial_app import views

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")