from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.


def register(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'welcome {username} your account has been created ')
            return redirect('login')
    else:
        form = RegisterForm
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html', {})
