from django.urls import path
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('password_reset', views.password_reset, name='password_reset'),
]

