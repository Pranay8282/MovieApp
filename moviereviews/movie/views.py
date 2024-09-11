from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movie,Review
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    searchTerm=request.GET.get('searchMovie')
    # movies=Movie.objects.all()
    if searchTerm:
        movies=Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies=Movie.objects.all()
    # return HttpResponse("<h1>Hey There.......</h1>")
    return render(request,"home.html",{'searchTerm':searchTerm,'movies':movies})


def about(request):
    return HttpResponse('<h1>Hey its an about page</h1>')


def signup(request):
    email=request.GET.get('email')
    return render(request,'signup.html',{'email':email})

def detail(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    reviews = Review.objects.filter(movie = movie)
    return render(request, 'detail.html',{'movie':movie,'reviews':reviews})


def createreview(request,movie_id):
    movie=get_object_or_404(Movie,pk=movie_id)
    
    if request.method=='GET':
        return render(request,'createreview.html',{'movie':movie})
    else:
        try:
            myreview=request.POST.get('myreview')
            newReview=Review()
            newReview.user=request.user
            newReview.movie=movie
            newReview.text=myreview
            newReview.save()
            return redirect('detail',newReview.movie.id)
        except ValueError:
            return render(request,'createreview.html',{'error':'Bad data passed in'})



def updatereview(request, review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    if request.method == 'GET':
        return render(request, 'updatereview.html', {'review': review})
    else:
        try:
            review.text = request.POST.get('myreview')
            review.save()
            return redirect('detail', review.movie.id)
        except ValueError:
            return render(request, 'updatereview.html', {'review': review,'error':'Bad data in form'})


def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id,user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)