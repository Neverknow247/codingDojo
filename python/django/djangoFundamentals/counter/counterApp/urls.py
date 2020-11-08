from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroySession', views.reset),
    path('add2', views.add2)
]