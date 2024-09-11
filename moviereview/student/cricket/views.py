from django.shortcuts import render
from .models import States
# Create your views here.


def cst(request):
    stat=States.objects.all()
    return render(request,'cricket.html',{'cricket':stat})