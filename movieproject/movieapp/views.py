from django.shortcuts import render, redirect

# Create your views here.
from . models import Movie
from . forms import Movieform

def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movi = Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movi})

def update(request,id):
    movie=Movie.objects.get(id=id)
    form =Movieform(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def add(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        year = request.POST.get('year', )
        desc = request.POST.get('desc', )
        duration = request.POST.get('duration', )
        genre = request.POST.get('genre', )
        img = request.FILES['image']
        starring = request.POST.get('starring', )
        movie = Movie(name=name, year=year, desc=desc, duration=duration, genre=genre, starring=starring, img=img)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')

def delete(request,id):
        if request.method==('POST'):
            movie=Movie.objects.get(id=id)
            movie.delete()

            return redirect('/')
        return render(request,'delete.html')
