from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
  return HttpResponse("My Health App")

def v1(response):
  return HttpResponse("View 1!")