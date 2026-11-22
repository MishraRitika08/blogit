from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterationForm, LoginForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('blog:home')
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  #auto login the user after registration
            messages.success(request, 'Registration successful and logged in!')
            return redirect('blog:home')
        else:
            messages.error(request, 'Registration failed. ')
    else:
        form = RegisterationForm()

    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('blog:dashboard')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('blog:home')
        else:   
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('blog:home')
