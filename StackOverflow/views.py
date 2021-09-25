from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect, HttpResponseRedirect, get_object_or_404
from .models import Question, Answer
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import QuestionForm, AnswerForm, CommentForm



def homepage(request):
    user=None
    if request.user.is_authenticated:
        user=request.user

    questions = Question.objects.all
    return render(request, "home.html", {'questions':questions, 'user': user})

def SignUp(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username , password = password)
            login(request,user)
            return redirect("/")
       

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

def question_detail(request, id):
    #form for answer
    form = AnswerForm()
    if request.method=='POST' and 'action' in request.POST :
        form = AnswerForm(request.POST)
        ans = form.save(commit=False)
        ans.question = Question.objects.get(id = id)
        ans.author_ans = User.objects.get(id = request.user.id)
        ans.save()

    #form for comment(ques)
    form_ques = CommentForm()
    if request.method=='POST' and 'action_ans' in request.POST :
        form_ques = CommentForm(request.POST)
        cmnt_ques = form_ques.save(commit=False)
        cmnt_ques.author_cmnt = User.objects.get(id = request.user.id)
        cmnt_ques.question = Question.objects.get(id = id)
        cmnt_ques.save()

     #form for comment(ans)
    form_ans = CommentForm()
    if request.method=='POST' and 'action_ans' in request.POST :
        form_ans = CommentForm(request.POST)
        cmnt_ans = form_ans.save(commit=False)
        cmnt_ans.author_cmnt = User.objects.get(id = request.user.id)
        cmnt_ans.answer = Answer.objects.get(id = id)
        cmnt_ans.save()
        

    ques = get_object_or_404(Question, id = id)
    if  request.user.is_authenticated:
        ques.views.add(request.user)
    
    return render(request, 'question_detail.html', {'ques': ques, 'form':form, 'form_ques':form_ques, 'form_ans':form_ans})

def ask_question(request):
    if request.user.is_authenticated:
        form = QuestionForm()
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            if form.is_valid():
                ques = form.save(commit=False)
                ques.author = User.objects.get(id = request.user.id)
                ques.save()         

        return render(request, 'ask_question.html', {'form' : form})
    else:
        return redirect("/SignIn")

def my_ques(request):
    if request.user.is_authenticated:
        questions = Question.objects.filter(author = request.user)
        return render(request, "my_ques.html", {'questions' : questions})
    else:
        return redirect("/SignIn")

def upvote_ans(request, id, q):
    
    ans = Answer.objects.get(id = id)
    ans.upvotes_ans.add(request.user)
    q = str(q)
    return redirect("/"+q+"/question_detail")

def upvote_ques(request, id):
    
    ques = Question.objects.get(id = id)
    ques.upvotes_ques.add(request.user)
    id= str(id)
    return redirect("/"+id+"/question_detail")

