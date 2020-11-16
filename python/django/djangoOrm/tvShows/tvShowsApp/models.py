from django.db import models

class showManager(models.Manager):
    def basicValidator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            if len(postData['desc']) > 0:
                errors['desc'] = "Description should be at least 10 characters"
        return errors

class shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    releaseDate = models.DateField()
    desc = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = showManager()
