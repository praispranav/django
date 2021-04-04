from django.shortcuts import render, redirect
from .models import Courses,Question,Lessons
from django.contrib.auth import authenticate
from .forms import userchoiceform

def courses(request):
    user = request.user
    if user.is_authenticated:
        course = Courses.objects.all()
        return render(request,'view2/courses.html',{'course':course})
    else:
        return redirect('/')

def lesson_view(request, course_id):
    user = request.user
    if user.is_authenticated:
        course = Courses.objects.get(id = course_id)    
        lesson = course.lessons_set.all()
        context = {
            'lesson':lesson,
            'course':course
        }
        return render(request,'view2/lessons.html',context)
    else:
        return redirect('/')

def questionlist(request,course_id,lesson_id):
    user= request.user
    if user.is_authenticated:
        course = Courses.objects.get(id = course_id)    
        lesson = course.lessons_set.get(id=lesson_id)
        question = lesson.question_set.all()
        context = {
            'question':question
        }
        
        return render(request,'view2/questionlist.html',context)
    else:
        return redirect('/')

def question_view(request,course_id,lesson_id,question_id):
    user= request.user
    if user.is_authenticated:
        course = Courses.objects.get(id = course_id)    
        lesson = course.lessons_set.get(id=lesson_id)
        question = lesson.question_set.get(id = question_id)
        choice = question.choice_set.all()
        form = userchoiceform()
        if request.method =='POST':
            form = userchoiceform(request.POST)
            if form.is_valid():
                form.save()
        context = {
            'form':form,
            'choice':choice,
            'question':question
        }
        
        return render(request,'view2/question.html',context)
    else:
        return redirect('/')