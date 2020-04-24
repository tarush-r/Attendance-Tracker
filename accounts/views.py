from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('/accounts/login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                print("username taken")
                return redirect('/accounts/register/')
            elif User.objects.filter(email=email).exists():
                print("email taken")
                messages.info(request, 'Email Taken')
                return redirect('/accounts/register/')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("usre saved")
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('/accounts/register/')
    else:
        return render(request, 'accounts/register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')