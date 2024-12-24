from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
  return HttpResponse("<h1>Hello there I am Basu from Django server</h1>")

def firstLession(req):
  return HttpResponse("<h1>Hi This is my first Lession</h1>")

def story(request):
  return render(request, 'index.html')

def htmlFile(request):
  return render(request, 'app/basu.html')