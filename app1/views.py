from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import signup_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ins_or_stu,Courses,Learner,Lessons,Enrollment,Instructor,online_course,online_course_submmision,Question,Choice,Submission
from .forms import profilesetupform,online_course_form,learnerform,instructorform


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect('/profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(username=username, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('/profile')
        else:
            return redirect('/')
    return render(request, 'index.html')

# signup form

def signup(request):
    user = request.user
    if user.is_authenticated:
        return redirect('/profile')
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username= username, password=raw_password)
            if user is not None:
                login(request,user)
                return redirect('/profilesetup')
            return redirect('/')
        else:
            return render(request,"<h1>Form Validation Failed</h1>")
        
    return render(request,'signup.html',{'form':form})

def profilesetup(request):
    user = request.user
    if user.is_authenticated:
        if ins_or_stu.objects.filter(user=user.id).exists():
            return redirect('/')
        else:
            form2 = profilesetupform()
            if request.method == 'POST':
                form2 = profilesetupform(request.POST)
                if form2.is_valid():
                    form2.save()
                    return redirect('/')
            return render(request,"profilesetupform.html",{'form2':form2})
    else: 
        return redirect('/')


# below is for instructor not learner.. only name laerner exists

def instructorprofilesetup(request):
    user = request.user
    if user.is_authenticated:
        if ins_or_stu.objects.get(user=user).ins == 2:
            if Instructor.objects.filter(user=user.id).exists():
                learner = Instructor.objects.get(user=user)
            else:
                learner = instructorform()
                if request.method == 'POST':
                    learner = instructorform(request.POST)
                    if learner.is_valid():
                        learner.save()
            context = {
                'learner':learner
            }
            return render(request,'instructorprofilesetup.html',context)
    

        


    
def logout_user(request):
    logout(request)
    return redirect('/')


def profile(request):
    user = request.user
    if user.is_authenticated:
        allCo = Courses.objects.all()
        try:
            if ins_or_stu.objects.get(user= request.user).ins == 1:
                if Learner.objects.filter(user=request.user.id).exists():
                        learner = Learner.objects.get(user=request.user)
                else:
                    learner = learnerform()
                    if request.method == 'POST':
                        learner = learnerform(request.POST)
                        if learner.is_valid():
                            learner.save()
                context = {
                    'learner':learner
                }
                return render(request,'learnerprofile.html',context)
            else:
                if Instructor.objects.filter(user=user).exists():
                    learner = Instructor.objects.get(user=request.user)
                    instructor = learner
                    courses = instructor.online_course_set.all()
                    form1 = online_course_form()
                    if request.method == 'POST':
                        # print(request.POST)
                        form1 = online_course_form(request.POST)
                        if form1.is_valid():
                            print(form1)
                            form1.save()
                    context= {
                        "learner":learner,
                        "form1":form1,
                        "courses":courses,
                        "allCo":allCo
                    }
                    return render(request,'profile.html',context)
                else:
                    return redirect('/instructorprofilesetup.html')
        except:
            return redirect('/profilesetup')    
    else:
        return redirect('/')


