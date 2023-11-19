from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def signup(request):
    username = ''

    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken. Choose a different username.')
            return redirect('signin')

        # Correct usage of create_user method
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('signin')

    return render(request, 'authentication/signup.html')

def signin(request):
      if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass1")

        User= authenticate(username=username,password=pass1)
        if  User is not None:
            login(request, User)
            fname=User.first_name
            return render(request,'base.html',{'fname': fname})
        else:
            messages.error(request,"bad credentials")
            return redirect('hm')

      return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect('hm')
