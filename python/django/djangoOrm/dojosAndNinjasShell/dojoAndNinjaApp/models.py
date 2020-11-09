from django.db import models

class dojos(models.Model):
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    desc = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class ninjas(models.Model):
    dojo = models.ForeignKey(dojos, related_name="ninja", on_delete= models.CASCADE)
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
