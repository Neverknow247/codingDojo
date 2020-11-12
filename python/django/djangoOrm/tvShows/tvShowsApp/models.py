from django.db import models

class shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    releaseDate = models.DateTimeField()
    desc = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
