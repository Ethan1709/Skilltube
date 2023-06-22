from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('uploader/<str:username>', views.user_videos, name='user_videos'),
    path('my_videos/<str:username>', views.my_videos, name='my_videos'),
    path('login', views.login_view, name='login'),
    path('registration/', views.signup, name='registration'),
    path('logout/', views.logout_view, name='logout'),
    path('search', views.category_search, name='search'),
    path('video_upload', views.upload, name='upload'),
    path('video/<str:video_id>', views.video_player, name='video')
]