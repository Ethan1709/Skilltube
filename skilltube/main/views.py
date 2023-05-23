from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Homepage skilltube view</h1>")

def video(response):
    return  HttpResponse("<h1>video playing page<h1>")