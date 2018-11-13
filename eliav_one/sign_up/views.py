from django.shortcuts import render
from sign_up.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):
    registered = False
    if request.method == "POST":
        userform = UserForm(data=request.POST)
        userform2 = UserProfileInfoForm(data=request.POST)
        if userform.is_valid() and userform2.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = userform2.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(userform.errors,userform2.errors)
    else:
        userform = UserForm()
        userform2 = UserProfileInfoForm()


    return render(request,template_name="sign_up/regist.html",context={'userform':userform,'userform2':userform2,'registered':registered})

@login_required
def special(request):
    return HttpResponse("YOU ARE LOGGED IN")

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('hello'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Login Failed!")
            print(f"username is {username}and password is {password}")
            return HttpResponse("Invalid Login Detailes")
    else:
        return render(request,'sign_up/login.html',context={'hi':'hello'})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('hello'))

def hello(request):
    return render(request,'sign_up/hello.html')
