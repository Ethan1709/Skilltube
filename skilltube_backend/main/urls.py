from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login_view, name='login'),
    path('registration/', views.signup, name='registration'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('search', views.search, name='search'),
    path('video_upload', views.upload, name='upload')
]