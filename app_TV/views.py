from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def index(request):
     context = {
          'shows': Show.objects.all()
     }
     return render(request,'shows.html', context)

def new(request):
     return render(request,'new.html')

def create(request):
     Show.objects.create(
          title = request.POST['title'],
          channel = request.POST['channel'],
          release_date = request.POST['release_date'],
          description = request.POST['description']
     )
     return redirect('/shows')

def edit(request, show_id):
     #query for one show only using id and edit 
     one_show = Show.objects.get(id = show_id)
     context = {
          'shows': one_show
     }
     return render(request, 'edit.html', context)
def update(request, show_id):
     update = Show.object.get(id = show_id)
     #update all fields
     update.title = request.POST['title']
     update.release_date = request.POST['release_date']
     update.channel = request.POST['channel']
     update.description = request.POST['description']
     update.save()
     return redirect('/shows/')

def delete(request, show_id):
     #query for one show only using id
     delete_one = Show.objects.get(id = show_id)
     delete_one.delete()
     return redirect('/shows')

def showid(request, show_id):
     #query for one show only using id
     one_show = Show.objects.get(id = show_id)
     context = {
          'showid': one_show
     }
     return render(request, 'showid.html', context)
