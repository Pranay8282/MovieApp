from django.shortcuts import render
from .models import stdata
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    stname=request.GET.get('stname')
    if stname:
        std=stdata.objects.filter(name__icontains=stname)
    else:
        std=stdata.objects.all()

    return render(request,'home.html',{'student':std})

    
def welcome(request):
    return render(request,'welcome.html')


def info(request,st_id):
    std=get_object_or_404(stdata,pk=st_id)
    return render(request,'information.html',{'student':std})