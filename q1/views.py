from django.shortcuts import render
from django.http import HttpResponse as s

# Create your views here.
def f(request):

    return render(request,'f.html')
def g(request):
    return render(request,'g.html')
def h(request):
    return render(request, 'h.html')


def i(request):
    return render(request, 'i.html')