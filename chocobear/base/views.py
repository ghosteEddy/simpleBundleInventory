from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def baseIndex(request):
    return HttpResponse("Hello")