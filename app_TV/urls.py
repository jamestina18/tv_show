from django.urls import path
from . import views 

urlpatterns = [
    #localhost: 8000/shows
    path('', views.index),
    #localhost: 8000/shows/new
    path('new', views.new),
    #localhost: 8000/shows/create
    path('create',views.create),
    #localhost: 8000/shows/<show_id>/edit  ex http://localhost:8000/shows/1/edit
    path('<int:show_id>/edit', views.edit),
     #update for the edit
    path('<int:show_id>', views.shows),
    #localhost: 8000/shows/<show_id>/edit
    path('<int:show_id>/update', views.update),
    #localhost: 8000/shows/<show_id>/  ex http://localhost:8000/shows/1
    path('<int:show_id>/delete', views.delete),
]
