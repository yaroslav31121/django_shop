from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import UserRegisterForm


def register(request):
    """
    View for user registration.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def get_success_url():
    """
    Returns the success URL for registration.
    """
    return reverse_lazy('index.html')


def password_reset(request):
    """
    View for password reset form.
    """
    return render(request, 'users/password_reset_form.html')


@login_required()
def profile(request):
    """
    View for user profile.
    """
    return render(request, 'users/profile.html')


@login_required()
def user_logout(request):
    """
    View for user logout.
    """
    logout(request)
    return redirect('login')
