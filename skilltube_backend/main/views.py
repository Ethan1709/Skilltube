from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Video
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, VideoForm
from django.contrib import messages
from . serializers import VideoSerializer
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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



def category_search(request):
    query = request.GET.get('category', '')
    search_query = request.GET.get('caption', '')

    search_results = Video.objects.filter(Q(category__icontains=query) & Q(caption__icontains=search_query))
    return render(request, 'search_results.html', {'search_results': search_results})


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            success_message = f'Hi {username}, your account has been successfully created.'
            return redirect(reverse('home') + '?success_message=' + success_message)
    else:
        form = UserRegisterForm()

    return render(request, 'registration.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            success_message = f"Welcome back, {user.username}!"
            return redirect(reverse('home') + f'?success_message={success_message}')

        else:
            error_message = "Invalid password or username"
            return redirect(reverse('login') + f'?error_message={error_message}')

    return render(request, 'login.html')


def upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = VideoForm()
      
    return render(request, 'video_upload.html', {'form':form})


def video_player(request, video_id):
    video = Video.objects.get(video_id=video_id)

    return render(request, 'video.html', {'video':video})
