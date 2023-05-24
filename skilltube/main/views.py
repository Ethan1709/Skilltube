from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def index(request):
    api_urls = {
        'videos': '/video/<video_id>'
    }

    return Response(api_urls)

def video(response):
    return HttpResponse('<h1>Video playing page</h1>')