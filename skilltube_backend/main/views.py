from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from .models import Video, Comment, Like
from .forms import UserRegisterForm, VideoForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseBadRequest

# Create your views here.


def index(request):
    video = Video.objects.all()
    return render(request, 'index.html',{'video':video})


def category_search(request):
    query = request.GET.get('category', '')
    search_query = request.GET.get('caption', '')

    search_results = Video.objects.filter(Q(category__icontains=query) & (Q(caption__icontains=search_query) | Q(user__username__icontains=search_query)))
    return render(request, 'search_results.html', {'search_results': search_results})


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user instance
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            
            # Store the token in the user model
            user.token = token
            user.save()
            
            username = form.cleaned_data.get('username')
            success_message = f'Hi {username}, your account has been successfully created.'

            user = authenticate(request, username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(reverse('home') + f'?success_message={success_message}&uid={uid}&token={token}')
    else:
        form = UserRegisterForm()

    return render(request, 'registration.html', {'form': form})


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


def logout_view(request):
    logout(request)
    success_message = 'You have been successfully logged out.'
    return redirect(reverse('home') + f'?success_message={success_message}')


@login_required
def upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user  # Assign the currently logged-in user to the video

            #Validate the caption length
            caption = form.cleaned_data['caption']
            if len(caption) > 22:
                error_message = 'Caption must be 22 or less caracters'
                return render(request, 'video_upload.html', {'form': form, 'error_message': error_message})

            # Validate video file type
            video_file = form.cleaned_data['video']
            if not video_file or not video_file.name.endswith(('.mp4', '.avi', '.mov')):
                error_message = 'Invalid video file type. Please upload a valid video file (MP4, AVI, MOV).'
                return render(request, 'video_upload.html', {'form': form, 'error_message': error_message})

            # Validate thumbnail file type
            thumbnail = form.cleaned_data['thumbnail']
            if not thumbnail or not thumbnail.name.endswith(('.jpg', '.jpeg', '.png')):
                error_message = 'Invalid thumbnail image file type. Please upload a valid image file (JPG, JPEG, PNG).'
                return render(request, 'video_upload.html', {'form': form, 'error_message': error_message})

            video.save()
            return redirect(reverse('home'))
    else:
        form = VideoForm()

    return render(request, 'video_upload.html', {'form': form})



def video_player(request, video_id):
    try:
        video = Video.objects.get(video_id=video_id)
    except Video.DoesNotExist:
        raise Http404("Video does not exist")

    comments = Comment.objects.filter(video=video)
    likes = Like.objects.filter(video=video)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                comment = form.save(commit=False)
                comment.video = video
                comment.user = request.user
                comment.save()
            else:
                error_message = 'You need to login to add a comment'
                return redirect(reverse('video', kwargs={'video_id': video_id}) + f'?error_message={error_message}')
    else:
        form = CommentForm()

    like_count = likes.count()
    user_liked = Like.objects.filter(video=video, user=request.user).exists() if request.user.is_authenticated else False

    context = {
        'video': video,
        'comments': comments,
        'form': form,
        'like_count': like_count,
        'user_liked': user_liked,
    }

    return render(request, 'video.html', context)



def my_videos(request, username):
    user = request.user
    if username != user.username:
        # Handle the case where the logged-in user is different from the username in the URL
        return HttpResponse('You are not authorized to view this page. Get out of here.')
    my_videos = Video.objects.filter(user=user)
    return render(request, 'my_videos.html', {'my_videos': my_videos})


def user_videos(request, username):
    video_user = Video.objects.filter(user__username=username)
    if not username or not video_user:
        return HttpResponse('This user does not exist')
    return render(request, 'uploader.html', {'video_user':video_user, 'username':username})


def require_POST(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.method != 'POST':
            return HttpResponseBadRequest('Only POST requests are allowed.')
        return view_func(request, *args, **kwargs)
    return wrapped_view


from django.http import HttpResponseBadRequest

@require_POST
def add_like(request, video_id):
    try:
        # Check if the video ID is valid and exists in your Video model
        video = Video.objects.get(video_id=video_id)
    except Video.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Invalid video ID'})

    # Check if the user is authenticated
    if not request.user.is_authenticated:
        error_message_like = 'You need to login to like a video'
        return redirect(reverse('video', kwargs={'video_id': video_id}) + f'?error_message_like={error_message_like}')

    # Check if the user has already liked the video
    user_liked = Like.objects.filter(video=video, user=request.user).exists()

    if user_liked:
        error_message_like = 'You already liked this video'
        return redirect(reverse('video', kwargs={'video_id': video_id}) + f'?error_message_like={error_message_like}')

    # Create a new Like object and save it
    like = Like(video=video, user=request.user)
    like.save()

    # Calculate the updated like count
    like_count = video.likes.count()

    # Return a success response with the updated like count and user_liked status
    success_message_like = 'Like added successfully'
    return redirect(reverse('video', kwargs={'video_id': video_id}) + f'?success_message_like={success_message_like}&like_count={like_count}&user_liked={user_liked}')
