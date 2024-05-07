from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


from .forms import CustomUserCreationForm
from .models import Quiz

@login_required
def mainpage(request):
    return render(request,'main/mainpage.html')

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

@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'main/quiz_list.html', {'quizzes': quizzes})