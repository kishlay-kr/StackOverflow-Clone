from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect, HttpResponseRedirect, get_object_or_404
from .models import Comment, Question, Answer
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.http import HttpResponseRedirect
from .forms import QuestionForm, AnswerForm, CommentForm




def homepage(request):
    user=None
    if request.user.is_anonymous:
        user = None 
    elif request.user.is_authenticated:
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
        # use AuthenticationForm()
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect("/SignIn" )
     
    else:
        user = None
        return render(request , "SignIn.html" , {'user':user})

def SignOut(request):
    logout(request)
    return redirect("/")

def question_detail(request, id):
    #form for answer
    form = AnswerForm()
    #form for comment(ques)
    form_ques = CommentForm()
    #form for comment(ans)
    form_ans = CommentForm()
    if request.method=='POST' and 'action' in request.POST :
        form = AnswerForm(request.POST)
        ans = form.save(commit=False)
        ans.question = Question.objects.get(id = id)
        ans.author_ans = User.objects.get(id = request.user.id)
        ans.save()
    elif request.method=='POST' and 'action_ques' in request.POST :     #*****************
        form_ques = CommentForm(request.POST)
        cmnt_ques = form_ques.save(commit=False)
        cmnt_ques.author_cmnt = User.objects.get(id = request.user.id)
        cmnt_ques.question = Question.objects.get(id = id)
        cmnt_ques.save()
     #form for comment(ans)
    elif request.method=='POST' and 'action_ans' in request.POST:
        form_ans = CommentForm(request.POST)
        print(request.POST)
        cmnt_ans = form_ans.save(commit=False)
        cmnt_ans.author_cmnt = User.objects.get(id = request.user.id)
        id_ans = request.POST.get('id_ans')
        cmnt_ans.answer = Answer.objects.get(id = id_ans)
        cmnt_ans.save()
        form_ans = CommentForm()
        

    ques = get_object_or_404(Question, id = id)
    if  request.user.is_authenticated:
        ques.views.add(request.user)
    else: 
        messages.error(request, 'Sign In to see the details of Question')
        return redirect("/SignIn")
    # user = User.objects.get(id = request.user.id)
    user = request.user
    return render(request, 'question_detail.html', {'ques': ques, 'form':form, 'form_ques':form_ques, 'form_ans':form_ans, 'user':user})

def ask_question(request):
    if request.user.is_authenticated:
        form = QuestionForm()
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            print(request.POST)
            if form.is_valid():
                ques = form.save(commit=False)
                print(ques.tags)
                ques.author = User.objects.get(id = request.user.id)
                ques.save()         

        return render(request, 'ask_question.html', {'form' : form})
    else:
        messages.error(request, 'Sign In to ask a Question ')
        return redirect("/SignIn")

def my_ques(request):
    if request.user.is_authenticated:
        questions = Question.objects.filter(author = request.user)
        return render(request, "my_ques.html", {'questions' : questions})
    else:

        messages.error(request, 'Sign In to view your Questions')
        return redirect("/SignIn")

def upvote_ans(request, id, q):
    
    ans = Answer.objects.get(id = id)
    ans.upvotes_ans.add(request.user)
    q = str(q)
    return redirect("/"+q+"/question_detail")

def unupvote_ans(request, id, q):
    ans = Answer.objects.get(id = id)
    ans.upvotes_ans.remove(request.user)
    q = str(q)
    return redirect("/"+q+"/question_detail")

def upvote_ques(request, id):
    
    ques = Question.objects.get(id = id)
    ques.upvotes_ques.add(request.user)
    id= str(id)
    return redirect("/"+id+"/question_detail")

def unupvote_ques(request, id):

    ques = Question.objects.get(id = id)
    ques.upvotes_ques.remove(request.user)
    id = str(id)
    return redirect("/"+id+"/question_detail")

def search(request):
    if request.user.is_anonymous:
        user = None
    else:
        user = request.user

    
    query = request.GET['search']
    questions = Question.objects.filter(tags__icontains=query)
    return render(request, 'search.html', {'questions':questions, 'user':user} )
    
def edit_ques(request,id):
    ques = Question.objects.get(id = id )   ##get_object_or_404
    

    if request.user == ques.author:
        form = QuestionForm()
        if request.method == 'POST':
            form = QuestionForm(request.POST, instance=ques)
            if form.is_valid():
                # ques = form.save(commit=False)
                # ques.save()      
                form.save() 
                return redirect("/"+str(id)+"/question_detail")  
        else:
            form = QuestionForm(instance=ques) ##*****************imp

        return render(request, 'edit_ques.html', {'form' : form , 'ques':ques})## put the contents of elements in the template of edit_question
    else:
        messages.error(request, 'Only the author has permission to edit ')
        return redirect("/"+str(id)+"/question_detail") ##show this error in question_detail template.

def edit_ans(request,id,q):
    ans = get_object_or_404(Answer, pk=id)
    ques = get_object_or_404(Question, pk=q)

    if request.user == ans.author_ans:
        if request.method == 'POST' :
            form = AnswerForm(request.POST , instance = ans)
            form.save()
            return redirect("/"+str(q)+"/question_detail")
        else:
            form = AnswerForm(instance = ans)
        
        return render(request, 'edit_ans.html', {'form':form, 'ans':ans, 'user':request.user})
    else:
        messages.error(request, 'Edit permissions denied')
        return redirect("/"+str(q)+"/question_detail")


def edit_cmnt(request,id,c):
    # ques = get_object_or_404(Question, pk=id)
    cmnt = get_object_or_404(Comment, pk=c)
    if request.user == cmnt.author_cmnt:
        if request.method == 'POST' :
            form = CommentForm(request.POST, instance = cmnt)
            form.save()
            return redirect('/'+str(id)+'/question_detail')
        else:
            form = CommentForm(instance = cmnt)
        return render(request, 'edit_cmnt.html', {'form':form, 'cmnt':cmnt})
    else:
        messages.error('Not allowed to edit')
        return redirect('/'+str(id)+'/question_detail')
