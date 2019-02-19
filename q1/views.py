from django.shortcuts import render
from django.http import HttpResponse as s
# Create your views here.
def index(request):
    return s("<p> INDEX </p>")
def Home(request):
    return s("<p> HOME</p>")
def Course(request):
    return s("<p> Course</p>")


