from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        allTasks = Task.objects.filter(userN=username)
        currentdate = timezone.now()
        params = {'allTasks': allTasks,'now': currentdate}
        return render(request,"todoApp/index.html",params)
def log(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            username = request.user.username
            taskName = request.POST.get("taskName","default")
            taskDesc = request.POST.get("taskDesc","default")
            taskDate = request.POST.get("taskDate","default")
            task = Task(taskName = taskName,desc = taskDesc,date = taskDate,userN=username)
            task.save()
            return redirect('index')
def delTask(request):
    taskid = request.GET.get('id')
    task = Task.objects.get(id=taskid)
    task.delete()
    return redirect('index')
def editTask(request):
    taskid = request.GET.get('id')
    task = Task.objects.get(id=taskid)
    params = {'task': task}
    task.delete()
    return render(request,'todoApp/edit.html',params)
def signUp(request):
    if request.method == 'POST':
        userName = request.POST.get('SuUsername')
        Fname = request.POST.get('SuFname')
        Lname = request.POST.get('SuLname')
        userEmail = request.POST.get('SuEmail')
        pass1 = request.POST.get('SuPass')
        pass2 = request.POST.get('SuPass2')

        existUser = User.objects.filter(username = userName)
        existEmail = User.objects.filter(email=userEmail)

        if len(userName) > 10:
            messages.error(request,'Username must be less than 10 characters')
            return redirect('home')
        if not pass1 == pass2:
            messages.error(request,'Both passwords didnt match, please try again')
            return redirect('home')
        if not userName.isalnum():
            messages.error(request,'Username should only contain alpha numeric characters')
            return redirect('home')
        if existUser:
            messages.error(request,'This username already exists please try a different one')
            return redirect('home')
        if existEmail:
            messages.error(request,'This email already exists please try a different one')
            return redirect('home')

            

        user = User.objects.create_user(username=userName,email=userEmail,password=pass1)
        user.first_name = Fname
        user.last_name = Lname
        user.save()
        messages.success(request,'Your account has been successfully created')
        return redirect('home')
    else:
        return HttpResponse('Error: 404(Not Found)')
    
def logIn(request):
    if request.method == 'POST':
        userName = request.POST.get('LogUsername')
        pass1 = request.POST.get('LogPass')

        user = authenticate(username = userName,password = pass1)
        if user is not None:
            login(request,user)
            messages.success(request,'You have been successfully logged in')
            return redirect('index')
        else:
            messages.error(request,'Sorry you entered wrong credentials please try again')
            return redirect('home')
def logOut(request):
    logout(request)
    messages.success(request,'You have successfully logged out')
    return redirect('home')




