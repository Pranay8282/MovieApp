from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import  User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
def signupaccount(request): 

    if request.method=='GET':
        return render(request, 'signup1.html',{'form':UserCreationForm})
    else:
        if request.POST['password1'] ==request.POST['password2']:
            try:
                user = User.objects.create_user(
                request.POST['username'],
                password= request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request,'signup1.html',{'form':UserCreationForm,'error':'Username already taken. Choosenew username.'})
        else:
            return render(request, 'signup1.html',{'form':UserCreationForm,'error':'Passwords do not match'})
        

def logoutaccount(request):
    logout(request)
    return redirect('home')


def loginaccount(request):
    if request.method =='GET':
        return render(request,'loginaccount.html',{'form':AuthenticationForm})
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html',{'form':AuthenticationForm,'error':'Account Not Found'})
        else:
            login(request,user)
            return redirect('home')