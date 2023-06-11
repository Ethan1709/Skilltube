from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Video
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from . serializers import VideoSerializer
from django.contrib.auth.decorators import login_required

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


def user_login(request):
    return render(request, 'login.html')

def search(request):
    query = request.GET.get('caption', '')
    
    search_results = Video.objects.filter(caption__icontains=query)
    
    context = {
        'search_results': search_results
    }
    
    return render(request, 'search_results.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account has been successfully created')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'registration.html', {'form':form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')