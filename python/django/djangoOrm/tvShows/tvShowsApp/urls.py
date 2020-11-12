from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.tvShows),
    path('shows/new', views.showNew),
    path('addShow', views.addShow),
    path('shows/<int:showNum>', views.showView),
]