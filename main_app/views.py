from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

class Plant:
  def __init__(self, name, type, height, age):
    self.name = name
    self.type = type
    self.height = height
    self.age = age