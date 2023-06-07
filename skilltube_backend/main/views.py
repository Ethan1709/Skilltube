from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Video
from . serializers import VideoSerializer

# Create your views here.

@api_view(['GET'])
def video_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    
def index(request):
    video = Video.objects.all()
    return render(request, 'index.html',{'video':video})


def user_registration(request):
    return render(request, 'registration.html')

def user_login(request):
    return render(request, 'login.html')

def search(request):
    query = request.GET.get('caption', '')
    
    search_results = Video.objects.filter(caption__icontains=query)
    
    context = {
        'search_results': search_results
    }
    
    return render(request, 'search_results.html', context)
