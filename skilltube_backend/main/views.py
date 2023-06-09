from django.shortcuts import render, redirect
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Video
from .models import Skilltube_user
from django import forms
from django.core.validators import MinLengthValidator
from . serializers import VideoSerializer

# Create your views here.

class SkilltubeUserForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(), validators=[MinLengthValidator(8)])

    class Meta:
        model = Skilltube_user
        fields = ['username', 'password', 'email']

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
        form = SkilltubeUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SkilltubeUserForm()
    return render(request, 'registration.html', {'form': form})