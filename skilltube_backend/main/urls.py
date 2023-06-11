from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.user_login, name='login'),
    path('search', views.search, name='search'),
    path('registration/', views.signup, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]