from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mainpage')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'main/signup.html', {'form': form})
