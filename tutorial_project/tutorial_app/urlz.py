from django.conf.urls import patterns, url 
from tutorial_app import views


# Create your views here
def index(request):
    return HttpResponse("Hello world!")