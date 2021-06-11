from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username =
    form = UserCreationForm
    return render(request, 'users/register.html', {'form': form})
