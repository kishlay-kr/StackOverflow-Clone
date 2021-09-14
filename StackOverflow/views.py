from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect, HttpResponseRedirect
from .models import Question
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.forms import UserCreationForm

from .forms import QuestionForm



def homepage(request):
    user=None
    if request.user.is_authenticated:
        user=request.user

    questions = Question.objects.all
    return render(request, "home.html", {'questions':questions, 'user': user})

def SignUp(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form.save
        return redirect("SignIn/")

    return render(request, "SignUp.html", {'form': form})

def SignIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username, password=password)
        if user is not None:
            login(request, user)
            print("\n\n\n")
            print(user)
            return redirect("/")
        else:
            messages.info(request, 'invalid user')
            return redirect("/")

    else:
        return render(request , "SignIn.html")
def SignOut(request):
    logout(request)
    return redirect("/")
