from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
# Create your views here.


def signupaccount(request):
    if request.method=='GET':
        return render(request,'signup11.html',{'form':UserCreationForm})
    else:
        
            if request.POST['password1']==request.POST['password2']:
                try:
                    user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                    user.save()
                    login(request,user)
                    return redirect('home')
                except IntegrityError:
                     return render(request,'signup11.html',{'form':UserCreationForm},{'error':'Username is already Taken'})
                
            else:
                 return render(request,'signup11.html',{'form':UserCreationForm},{'error':'Enter DIff Password'})
            

def logoutaccount(request):
     logout(request)
     return redirect('home')



def loginaccount(request):
    if request.method=='GET':
         return render(request,'login11.html',{'form':AuthenticationForm})
    else:
          user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
          if user is None:
              return render(request,'login11.html',{'form':AuthenticationForm,'error':"Invalid Un nd pass"})
          else:
               login(request,user)
               return redirect('home')
