from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


from .forms import CustomUserCreationForm
from .models import Quiz,Question,Option

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

@login_required
def quiz_details(request, quiz_id):
    quiz = Quiz.objects.filter(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz_id)
    options = Option.objects.all()
    return render(request, 'main/quiz_details.html', {'quiz':quiz, 'questions':questions, 'options':options})