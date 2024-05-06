from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/',auth_views.LoginView.as_view(template_name='main/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='mainpage'), name="logout"),
]