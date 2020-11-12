from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addAuthor', views.addAuthor),
    path('books/<int:bookNum>', views.bookView),
    path('authors/<int:authorNum>', views.authorView),
    path('bookAdd', views.bookAdd),
    path('authorAdd', views.authorAdd),
    path('addAuthorToBook/<int:bookNum>', views.addAuthorToBook),
    path('addBookToAuthor/<int:authorNum>', views.addBookToAuthor),

]