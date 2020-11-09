from django.db import models

class users(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    age = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
