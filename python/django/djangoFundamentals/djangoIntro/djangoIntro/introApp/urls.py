from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('nba', views.showNbaHome),
    path('nba/lol', views.lol),
    path('nba/<int:val>', views.anotherMethod),
    path('google',views.google),
    path('nfl',views.nfl),
    path('redir', views.redir),
]