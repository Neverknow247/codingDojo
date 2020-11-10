from django.db import models

class books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class authors(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    books = models.ManyToManyField(books, related_name="author")
    notes = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
